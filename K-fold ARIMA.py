from datetime import date
from datetime import timedelta
import pandas as pd
import pyramid.arima as pm
import matplotlib.pyplot as plt

# reading in data
from sklearn.metrics import mean_squared_error
from numpy import sqrt, mean

df = pd.read_csv("AMZN.csv") # select the dataset

df = pd.DataFrame.drop(df, labels=['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1) # don't need these features (you might, if so, keep it.)


df.TimeStamp = pd.to_datetime(df['Date'], format='%Y/%m/%d')
df.index = df.TimeStamp
df = df.resample('D').mean()  # to fill in missing dates
df = df.interpolate()  # to fill NaN values

# For 10 cross validation : 9 sets of training data (each starts from first day to end of each time period) Time period = 36 days
# 9 Sets of test data starting from second interval to last interval


TrainSetlist = list()
d = date(2017, 9, 11)
d = d + timedelta(36)
for i in range(0, 9):
    TrainSetlist.append(df['2017-09-11':d])
    d = d + timedelta(36)

print(TrainSetlist[8])
d = date(2017, 9, 11)
d = d + timedelta(36)

TestSetList = list()  # Each test set will contain 36 days data that is going to predicted by training on the entire interval before it

for i in range(0, 9):
    TestSetList.append(df[d:d + timedelta(36)])
    d = d + timedelta(36)

print(TestSetList[8])
# TestSetList.append(df[d:])


forecast = list()
for i in range(0, 9):
    print("For the set : ")
    print(i + 1)
    model = pm.auto_arima(TrainSetlist[i], max_p=5, max_q=5, m=7, seasonal=True,
                          trace=True, error_action='ignore', suppress_warnings=True, stepwise=True)
    print('AIC : ', model.aic())
    forecast.append(model.predict(n_periods=37))

error = list()

for i in range(0, 9):
    next_period_forecast = pd.DataFrame(forecast[i], index=TestSetList[i].index, columns=['Predictions'])

    # calculating error in each set

    rmse = sqrt(mean_squared_error(TestSetList[i].Close, forecast[i]))
    error.append(rmse)

    plt.figure(figsize=(16, 8))
    plt.plot(TrainSetlist[i].Close, label='Train')
    plt.plot(TestSetList[i].Close, label='Test')
    plt.plot(next_period_forecast.Predictions, label='Predictions')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend(loc='best')
    plt.show()

print(error)
print('MEAN ERROR : ', mean(error))

