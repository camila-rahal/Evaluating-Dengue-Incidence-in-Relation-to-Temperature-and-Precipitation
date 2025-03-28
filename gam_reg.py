from pygam import LinearGAM, s
import numpy as np
import matplotlib.pyplot as plt

# Define predictors and response variable
X = df_model[["temp_mean_lag1", "humidity_mean_lag1"]].values
y = np.log1p(df_model["monthly_cases"])  # Log transformation for stability

# Fit a GAM model with smooth functions
gam = LinearGAM(s(0) + s(1)).fit(X, y)

# Print summary
print(gam.summary())

# Plot smooth effects
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
titles = ["Effect of Temperature (Lag 1)", "Effect of Humidity (Lag 1)"]

for i, ax in enumerate(axs):
    XX = gam.generate_X_grid(term=i)
    ax.plot(XX[:, i], gam.partial_dependence(term=i, X=XX))
    ax.set_title(titles[i])

plt.show()
