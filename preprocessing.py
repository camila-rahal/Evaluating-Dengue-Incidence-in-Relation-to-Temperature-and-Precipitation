##------------------------------------------------------------------------------------##
##----------------------- Dengue, Temp & Umidity data - month ------------------------##
##------------------------------------------------------------------------------------##

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

# Imputation of missing values with interpolation
monthly_merged.interpolate(method="linear", inplace=True)

# Export
monthly_merged.to_csv("bauru_dengue_monthly_combined.csv", index=False)
print("Done! Saved to bauru_dengue_monthly_combined.csv")

##------------------------------------------------------------------------------------##
##------------------------------Precipitation data------------------------------------##
##------------------------------------------------------------------------------------##

import pandas as pd

# Define the dataset structure
columns = ["Ano", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
data = [
    [2025, 225.8, 70.1, None, None, None, None, None, None, None, None, None, None],
    [2024, 208.8, 138.2, 184.7, 109.2, 22.9, 1.0, 22.4, 30.2, 11.7, 126.2, 237.7, 286.3],
    [2023, 295.7, 270.5, 210.1, 70.1, 62.7, 71.1, 0.5, 22.1, 19.1, 143.0, 98.6, 103.6],
    [2022, 426.5, 150.4, 176.0, 27.2, 44.7, 91.7, 1.3, 33.5, 86.6, 100.1, 60.2, 339.9],
    [2021, 181.9, 169.9, 125.7, 33.3, 19.6, 46.7, 10.4, 15.0, 14.7, 130.8, 201.9, 215.4],
    [2020, 211.1, 366.0, 14.7, 23.4, 33.5, 75.9, 9.4, 69.9, 7.9, 40.4, 70.1, 467.1],
    [2019, 176.3, 185.2, 273.1, 82.8, 14.7, 13.2, 31.2, 11.2, 43.4, 59.7, 168.9, 217.2],
    [2018, 258.8, 98.8, 258.1, 15.0, 10.7, 15.7, 4.6, 124.7, 91.4, 180.8, 137.9, 198.9],
    [2017, 462.0, 137.9, 135.9, 119.1, 218.7, 22.4, 0.0, 66.3, 16.5, 117.9, 263.4, 95.0],
    [2016, 380.2, 351.3, 118.9, 37.8, 110.2, 94.0, 9.1, 61.7, 24.6, 103.6, 91.2, 143.8],
    [2015, 182.4, 134.1, 251.5, 46.7, 125.2, 0.0, 88.1, 21.6, 220.2, 123.4, 260.1, 259.8],
    [2014, 104.6, 132.3, 125.5, 74.4, 63.8, 0.5, 30.5, 22.4, 125.0, 37.3, 116.6, 257.0],
    [2013, 284.0, 162.8, 192.0, 105.9, 144.8, 78.0, 39.9, 0.0, 66.3, 135.1, 171.2, 54.6],
    [2012, 262.1, 81.8, 177.0, 192.3, 83.8, 197.6, 11.4, 0.0, 94.7, 51.8, 138.2, 121.9],
    [2011, 496.1, 173.7, 144.5, 89.2, 31.5, 45.7, 7.9, 40.4, 3.0, 209.3, 135.9, 207.5],
    [2010, 213.4, 42.7, 55.1, 88.9, 33.0, 29.2, 88.6, 0.0, 92.7, 132.6, 86.4, 218.9],
    [2009, 253.7, 149.1, 117.1, 8.1, 45.0, 51.6, 67.8, 91.4, 121.2, 130.1, 229.9, 319.5],
    [2008, 213.4, 149.9, 92.2, 125.2, 73.9, 58.2, 0.0, 54.1, 29.7, 129.8, 107.9, 132.3],
    [2007, 327.2, 177.0, 42.4, 55.9, 45.0, 3.3, 239.5, 0.0, 3.0, 51.3, 219.7, 182.6],
    [2006, 166.1, 263.1, 43.7, 12.2, 13.7, 12.2, 34.3, 15.5, 62.5, 7.4, 65.5, 251.0],
    [2005, 363.2, 89.4, 119.6, 21.3, 70.4, 47.2, 7.1, 16.5, 39.4, 10.7, 63.8, 190.2],
    [2004, 189.0, 137.2, 48.3, 65.8, 105.4, 16.0, 43.9, 0.0, 4.1, 98.8, 11.7, 174.2],
    [2003, 366.3, 138.2, 84.3, 158.8, 34.8, 47.2, 12.4, 29.7, 14.5, 82.3, 138.2, 202.9],
    [2002, 158.2, 196.3, 24.4, 17.3, 81.0, 0.0, 33.8, 52.6, None, 14.7, 122.7, 169.9],
    [2001, 310.6, 188.7, 115.3, 11.2, 77.7, 45.7, 38.6, 42.2, 26.9, 45.2, 35.1, 231.6],
]

# Create a DataFrame
precipitation = pd.DataFrame(data, columns=columns)

precipitation = precipitation.drop(index=[0, 1, 2, 3, 4, 16, 17, 18, 19, 20, 21, 22, 23, 24])

#print(precipitation)

# Save as CSV
csv_filename = "precipitation_data.csv"
precipitation.to_csv(csv_filename, index=False)


##------------------------------------------------------------------------------##

# Transform the DataFrame to long format (melt)
df_melted = precipitation.melt(id_vars=["Ano"], var_name="Month", value_name="precipitation")

# Convert month names to numerical format
month_map = {
    "Jan": "01", "Fev": "02", "Mar": "03", "Abr": "04",
    "Mai": "05", "Jun": "06", "Jul": "07", "Ago": "08",
    "Set": "09", "Out": "10", "Nov": "11", "Dez": "12"
}

df_melted["Month"] = df_melted["Month"].map(month_map)

# Create a datetime column
df_melted["month_year"] = pd.to_datetime(df_melted["Ano"].astype(str) + "-" + df_melted["Month"] + "-01")

# Select relevant columns
df_melted = df_melted[["month_year", "precipitation"]].sort_values(by="month_year")

# Save as CSV
csv_filename_long = "precipitation_long_format.csv"
df_melted.to_csv(csv_filename_long, index=False)

##----------------------------------- Merge DataFrames -------------------------------------------##

df_merge = monthly_merged.merge(df_melted, on="month_year", how="left")

print(df_merge["precipitation"].isnull().sum())

monthly_merged["month_year"] = pd.to_datetime(monthly_merged["month_year"])
df_melted["month_year"] = pd.to_datetime(df_melted["month_year"])

# Check the mean and variance of the "monthly_cases" variable (Poisson assumption)
mean_cases = df_merge["monthly_cases"].mean()
variance_cases = df_merge["monthly_cases"].var()

print(mean_cases)
print(variance_cases)

print(df.dtypes)

csv_filename_merged = "data.csv"
df_merge.to_csv(csv_filename_merged, index=False)




##------------------------------- Finite Distributed Lagged -----------------------------------##


# Load your dataset
df = pd.read_csv("data.csv", parse_dates=["month_year"])

# Sort by month_year to ensure proper lagging
df = df.sort_values("month_year")

# Create lagged variables (one-month lag)
df["temp_mean_lag1"] = df["temp_mean"].shift(1)
df["humidity_mean_lag1"] = df["humidity_mean"].shift(1)
df["precipitation_lag1"] = df["precipitation"].shift(1)

# Save the updated dataset
df.to_csv("data_with_lags.csv", index=False)

print("Lagged variables added! Saved to data_with_lags.csv")


##------------------------------------------------------------------------------------##
##----------------------- Dengue, Temp & Umidity data - weekly -----------------------##
##------------------------------------------------------------------------------------##

# Load data
df_week = pd.read_csv("dengue_bauru.csv")

# Convert to datetime
df_week["data_iniSE"] = pd.to_datetime(df["data_iniSE"], errors="coerce")
df_week = df_week.dropna(subset=["data_iniSE"])

# Keep weekly timestamp instead of aggregating to monthly
df_week["week"] = df_week["data_iniSE"].dt.to_period("W").dt.to_timestamp()

# Aggregate dengue cases at the weekly level
weekly_cases = df_week.groupby("week", as_index=False)["casos"].sum()

# Aggregate climate data at the weekly level using means
weekly_climate = df_week.groupby("week", as_index=False)[
    ["tempmed", "tempmin", "tempmax", "umidmed", "umidmin", "umidmax"]
].mean()

# Merge datasets
weekly_merged = pd.merge(weekly_cases, weekly_climate, on="week")

# Rename columns for clarity
weekly_merged.rename(columns={
    "week": "week_year",
    "casos": "weekly_cases",
    "tempmed": "temp_mean",
    "umidmed": "humidity_mean",
    "umidmin": "humidity_min",
    "umidmax": "humidity_max"
}, inplace=True)

# Impute missing values with linear interpolation
weekly_merged.interpolate(method="linear", inplace=True)

# Export the cleaned weekly dataset
weekly_merged.to_csv("bauru_dengue_weekly_combined.csv", index=False)
print("Done! Saved to bauru_dengue_weekly_combined.csv")