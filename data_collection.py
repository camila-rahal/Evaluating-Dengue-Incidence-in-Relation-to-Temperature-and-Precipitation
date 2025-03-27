import os
import re
import time
import zipfile
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from PyPDF2 import PdfReader

# Create a working directory
Path("data").mkdir(parents=True, exist_ok=True)
os.chdir("data")


# --- Scrape INMET historical meteorological data page ---

inmet_url = "https://portal.inmet.gov.br/dadoshistoricos"
response = requests.get(inmet_url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract all links with text containing "ANO"
links = [a.get("href") for a in soup.find_all("a") if "ANO" in a.get_text()]
base_url = "https://portal.inmet.gov.br/uploads/dadoshistoricos/"

# Download and unzip each link with retry logic
def download_and_unzip(link):
    match = re.search(r"/(\d{4})\.zip", link)
    if not match:
        return
    year = match.group(1)
    zip_filename = f"ANO_{year}.zip"
    unzip_dir = f"ANO_{year}"
    download_url = f"{base_url}{year}.zip"
    
    attempts, success = 0, False
    while not success and attempts < 3:
        try:
            print(f"Attempting download: {download_url}")
            r = requests.get(download_url, stream=True)
            with open(zip_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            success = True
        except Exception as e:
            print(f"Error downloading {year}: {e}")
            attempts += 1
            time.sleep(5)

    if success:
        try:
            with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
            print(f"Unzipped: {zip_filename}")
        except Exception as e:
            print(f"Error unzipping {zip_filename}: {e}")
            os.remove(zip_filename)

# Loop through each year-link and process
for link in links:
    download_and_unzip(link)

# Remove all .zip files after extraction
for file in os.listdir():
    if file.endswith(".zip"):
        os.remove(file)

print("All zip files deleted.")
