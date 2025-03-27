import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("bauru_dengue_monthly_combined.csv")

# 2. Convert date column to datetime and set index
df["month_year"] = pd.to_datetime(df["month_year"])
df.set_index("month_year", inplace=True)

# 3. Create 1-month lagged climate variables
df["temp_mean_lag1"] = df["temp_mean"].shift(1)
df["humidity_mean_lag1"] = df["humidity_mean"].shift(1)

# 4. Optional: Log-transform the target to stabilize variance
df["log_cases"] = np.log1p(df["monthly_cases"])  # log(1 + cases)

# 5. Drop rows with NA from lagging
df_model = df.dropna(subset=["temp_mean_lag1", "humidity_mean_lag1", "monthly_cases", "log_cases"])

# 6. Define predictors and target
X = df_model[["temp_mean_lag1", "humidity_mean_lag1"]]
X = sm.add_constant(X)  # Adds intercept term

# Linear regression with raw case counts
y = df_model["monthly_cases"]
model_raw = sm.OLS(y, X).fit()

# Linear regression with log-transformed case counts
y_log = df_model["log_cases"]
model_log = sm.OLS(y_log, X).fit()

# 7. Print model summaries
print("=== Linear Regression on Raw Monthly Cases ===")
print(model_raw.summary())

print("\n=== Linear Regression on Log-Transformed Monthly Cases ===")
print(model_log.summary())

# 8. Optional: Plot actual vs. predicted for log model
df_model["predicted_log_cases"] = model_log.predict(X)
df_model["predicted_cases"] = np.expm1(df_model["predicted_log_cases"])

plt.figure(figsize=(12, 5))
plt.plot(df_model.index, df_model["monthly_cases"], label="Actual Cases")
plt.plot(df_model.index, df_model["predicted_cases"], label="Predicted Cases (log model)")
plt.title("Actual vs Predicted Dengue Cases (Log Model)")
plt.xlabel("Month")
plt.ylabel("Monthly Cases")
plt.legend()
plt.tight_layout()
plt.show()
