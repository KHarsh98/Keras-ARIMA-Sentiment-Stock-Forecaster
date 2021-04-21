
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

# IMPORTING DATA


df = pd.read_csv("AMZN.csv")

df["Adj Close"].plot(figsize=(15, 8), title="NVR")

df['RM Close'] = df['Adj Close'].rolling(3, win_type='triang').mean()
df['RM Close'].plot(figsize=(15, 8), title="NVR")

plt.show()

# CREATING train and test set (11/1)


train = df[0:223]
test = df[223:]

df.Timestamp = pd.to_datetime(df.Date, format='%Y/%m/%d')
df.index = df.Timestamp
df = df.resample('D').mean()
df.interpolate()
train.Timestamp = pd.to_datetime(train.Date, format='%Y/%m/%d')
train.index = train.Timestamp
train = train.resample('D').mean()

test.Timestamp = pd.to_datetime(test.Date, format='%Y/%m/%d')
test.index = test.Timestamp
test = test.resample('D').mean()


# Plotting data

df['Close'].plot(figsize=(16,8), title = "Peaks")

import statsmodels.api as sm

# Fitting on ARIMA
y_hat_avg = test.copy()
fit1 = sm.tsa.statespace.SARIMAX(train['RM Close'], order=(2,2,2), seasonal_order=(0,1,1,7)).fit()
y_hat_avg['SARIMA'] = fit1.predict(start="2018-08-01", end = "2018-08-31",dynamic=True)



plt.figure(figsize=(16, 8))
plt.plot(train['RM Close'], label = 'Train')
plt.plot(test['RM Close'], label = 'Test')
plt.plot(y_hat_avg['SARIMA'], label='SARIMA')
plt.legend(loc='best')
plt.show()

from sklearn.metrics import mean_squared_error
from math import sqrt


rms = sqrt(mean_squared_error(test['RM Close'], y_hat_avg.SARIMA))
print(rms)
