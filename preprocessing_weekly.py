##----------------------- Dengue, Temp & Humidity data - weekly -----------------------##
##------------------------------------------------------------------------------------##
import pandas as pd

# Load data
df_week = pd.read_csv("dengue_bauru.csv")

# Convert to datetime
df_week["data_iniSE"] = pd.to_datetime(df_week["data_iniSE"], errors="coerce")
df_week = df_week.dropna(subset=["data_iniSE"])

# Keep weekly timestamp instead of aggregating to monthly
df_week["week"] = df_week["data_iniSE"].dt.to_period("W").dt.to_timestamp()

df_week.rename(columns={"data_iniSE":"week_year"}, inplace=True)

df_week = df_week.loc[:, ["week_year", "casos", "tempmed", "umidmed"]]

# Impute missing values with linear interpolation
df_week.interpolate(method="linear", inplace=True)

# Create lag variables (1-week lag)
df_week["casos_lag1"] = df_week["casos"].shift(1)
df_week["tempmed_lag1"] = df_week["tempmed"].shift(1)
df_week["umidmed_lag1"] = df_week["umidmed"].shift(1)

# Export the cleaned weekly dataset
df_week.to_csv("bauru_dengue_weekly.csv", index=False)
print("Done! Saved to bauru_dengue_weekly.csv")