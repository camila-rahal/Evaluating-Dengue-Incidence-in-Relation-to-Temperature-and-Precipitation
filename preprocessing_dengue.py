import pandas as pd

# Load data
df = pd.read_csv("dengue_bauru.csv")

# Convert to datetime
df["data_iniSE"] = pd.to_datetime(df["data_iniSE"], errors="coerce")
df = df.dropna(subset=["data_iniSE"])

import pandas as pd

# Load data
df = pd.read_csv("dengue_bauru.csv")

# Convert to datetime
df["data_iniSE"] = pd.to_datetime(df["data_iniSE"], errors="coerce")
df = df.dropna(subset=["data_iniSE"])

# Create monthly timestamp
df["month"] = df["data_iniSE"].dt.to_period("M").dt.to_timestamp()

# Aggregate dengue cases
monthly_cases = df.groupby("month", as_index=False)["casos"].sum()

# Aggregate climate data using correct column names
monthly_climate = df.groupby("month", as_index=False)[
    ["tempmed", "tempmin", "tempmax", "umidmed", "umidmin", "umidmax"]
].mean()

# Merge datasets
monthly_merged = pd.merge(monthly_cases, monthly_climate, on="month")

# Rename columns for clarity
monthly_merged.rename(columns={
    "month": "month_year",
    "casos": "monthly_cases",
    "tempmed": "temp_mean",
    "umidmed": "humidity_mean",
    "umidmin": "humidity_min",
    "umidmax": "humidity_max"
}, inplace=True)

# Export
monthly_merged.to_csv("bauru_dengue_monthly_combined.csv", index=False)
print("Done! Saved to bauru_dengue_monthly_combined.csv")
