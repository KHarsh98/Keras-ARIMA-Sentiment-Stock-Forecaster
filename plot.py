import pandas as pd
import numpy as np

# IMPORT DATA

data = pd.read_csv('data_stocks.csv')

data = data.drop(['DATE'], 1)

# Dimensions of data
n = data.shape[0]
p = data.shape[1]

data = data.values
from matplotlib import pyplot

pyplot.plot(data['SP500'])


