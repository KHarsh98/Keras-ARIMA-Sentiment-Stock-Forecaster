from datetime import date
import pandas as pd
import pyramid.arima as pm

import matplotlib.pyplot as plt

# reading in data
from numpy.ma import sqrt
from sklearn.metrics import mean_squared_error

df = pd.read_csv("AMZN.csv")

df = pd.DataFrame.drop(df, labels=['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)

df.TimeStamp = pd.to_datetime(df['Date'], format='%Y/%m/%d')
df.index = df.TimeStamp
df = df.resample('D').mean()  # to fill in missing dates
df = df.interpolate() #to fill NaN values

train = df['2018-10-20':'2018-12-31']
test = df['2015-05-26':'2015-06-26']

from pyramid import utils
utils.plot_acf(train)
utils.plot_pacf(train)
'''
model = pm.auto_arima(train, max_p=5,  max_q=5, m=7, seasonal=True,
                      trace=True, error_action='ignore', suppress_warnings=True, stepwise=True)

print('AIC = ', model.aic())

forecast = model.predict(n_periods=32)

forecast = pd.DataFrame(forecast, index=test.index, columns=['Predictions'])

rmse = sqrt(mean_squared_error(forecast['Predictions'], test['Close']))

print('RMSE = ', rmse)
plt.figure(figsize=(14, 6))
plt.plot(train.Close, label="TRAIN")
plt.plot(forecast.Predictions, label='FORECAST')
plt.plot(test.Close, label='TEST')
plt.legend(loc='best')
plt.show()

forecast.to_csv('FORECAST DJAI.csv', index = False)


'''