# Modeling the Association Between Climatic Conditions and Dengue Incidence Using Monthly Surveillance Data in Bauru, 2010–2018

This project is a improvement of another project done previously in R here: https://github.com/camilarahal/uni-capstone-project-dengue

This project was done with Python version 3.12

Requirements:

- - pip install pandas
- - pip install PyPDF2
- - pip install openpyxl
- - pip install statsmodels
- - pip install matplotlib

# Dataset:
- - Precipitation data: https://www.ipmetradar.com.br/2estHist.php
- - Cases, temperature and umidity data: https://info.dengue.mat.br/services/api

# Files:

- 1_report.pdf: full report with results and interpretations.
- preprocessing.py: preprocessing data with cases, temperature, humidity and precipitation for monthly model.
- preprocessing_weekly.py: preprocessing data with cases, temperature and humidity for weekly model.
- regression.py: regression for both monthly and weekly models.