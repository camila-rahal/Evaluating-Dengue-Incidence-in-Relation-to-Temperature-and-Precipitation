import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load dataset
df = pd.read_csv("data_with_lags.csv")  # Replace with the actual filename

# Drop rows with missing values (first row due to lag variables)
df = df.dropna()

# Define the formula for the Negative Binomial Model
formula = "monthly_cases ~ temp_mean_lag1 + humidity_mean_lag1 + precipitation_lag1"

# Fit the Negative Binomial Regression Model
model = smf.glm(formula=formula, data=df, family=sm.families.NegativeBinomial()).fit()

# Print the model summary
print(model.summary())
