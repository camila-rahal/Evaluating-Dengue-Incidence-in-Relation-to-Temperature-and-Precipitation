# Modeling the Association Between Climatic Conditions and Dengue Incidence Using Monthly Surveillance Data in Bauru, 2010–2018


This project is a improvement of another project done previously in R here: https://github.com/camilarahal/uni-capstone-project-dengue

This project was done with Python version 3.12

Requirements:

pip install pandas
pip install requests
pip install beautifulsoup4
pip install PyPDF2
pip install openpyxl
pip install statsmodels
pip install matplotlib
pip install pygam
pip install selenium

Data used was from Bauru: variables: 

cases: Number of notified cases per week (values ​​are retrospectively updated every week)
tempmean: Average daily temperatures along the week
humidmean: Average daily relative air humidity along the week
precipitation: Precipition acumulated per month

About cases data: Where does the data come from?
• Reported cases of dengue, zika or chikungunya. These are notifiable diseases, that is, the health worker diagnosing a suspicious case needs to fill out a notification form that feeds a municipal database which is then consolidated at the state level and finally, federally by the Ministry of Health. Only a fraction of these cases are laboratory confirmed, most receive final classification based on clinical and epidemiological criteria. From the notified cases, the incidence indicators that feed the InfoDengue are calculated.

About climate data:

To model the dengue fever incidence, several climatic
factors were used as explanatory variables. Data for monthly
climatic variables were collected from both the IMPET Radar and on the InfoDengue.

precipitation data: https://www.ipmetradar.com.br/2estHist.php
cases, temperature and umidity data: https://info.dengue.mat.br/services/api

# Preprocessing:

Data was first collected, then, the weekly climate and dengue fever cases were aggregated to month/year. Then, precipitation data was merged to the dataset.

Missing values related to climate were impute with interpolation, a method used commonly for temporal dataset. (https://www.e-education.psu.edu/meteo810/content/l5_p4.html).

Negative Binomial Regression is chosen because the variance (3,064,512.39) is significantly greater than the mean (556.66), indicating overdispersion, which violates the Poisson assumption of equal mean and variance.

 It was introduced one-month lagged climate variables (temperature, humidity, and precipitation) to account for the delayed effect of environmental conditions on dengue transmission. 
 

 The Negative Binomial regression model suggests that temperature and humidity (lagged by one month) are significantly associated with monthly dengue cases, as their p-values are <0.001. The coefficient for temperature (0.3719) indicates that higher temperatures increase dengue cases, while humidity (0.1198) also has a positive effect. Precipitation (-0.0015), however, is not statistically significant (p=0.219), meaning it does not have a clear effect on dengue cases in this model. The model explains about 79.56% of the variability in dengue cases (Pseudo R² = 0.7956), and the log-likelihood (-856.19) indicates a reasonably good fit.
 
 Discussion: Ideally this would be introduced per week lagged, which aligns with mosquitoes Aedes Aegypti life cycle (7-10 days), but due to precipitation data not being available per week, this study defined one-month lagged variables instead.



