import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load dataset
df = pd.read_csv("data_with_lags.csv") 

# Drop rows with missing values (first row due to lag variables)
df = df.dropna()

# Define the formula for the Negative Binomial Model
formula = "monthly_cases ~ temp_mean_lag1 + humidity_mean_lag1 + precipitation_lag1"

# Fit the Negative Binomial Regression Model
model = smf.glm(formula=formula, data=df, family=sm.families.NegativeBinomial()).fit()

# Print the model summary
print(model.summary())

##------------------------------- Weekly temp and humidity data----------------------------------##

# Load dataset
df_week = pd.read_csv("bauru_dengue_weekly.csv") 

import statsmodels.api as sm
import statsmodels.formula.api as smf

# Drop NaN values (created by lagging)
df_week = df_week.dropna()

# Define the model formula
formula = "casos ~ tempmed_lag1 + umidmed_lag1 + casos_lag1"

# Fit the Negative Binomial model
model_nb = smf.glm(formula=formula, data=df_week, 
                    family=sm.families.NegativeBinomial()).fit()

# Print the results
print(model_nb.summary())


