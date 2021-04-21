import keras
import pandas as pd
import tensorflow as tf

#DATA PREPROCESSING

'''
        Note : This CSV file is created through running ARIMA and sentiment polarities from the sentiment analyser.
                Please run ARIMA and SentimentAnalyser first.
'''
data = pd.read_csv("SentStock.csv") # SentStock = sentiment polarities + stock prices

test = data['Output Price'].copy()

train = data.drop(['Output Price'], axis = 1)

print(train.isnull().any())

print(test.isnull().any())

X = train.values
Y = test.values

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler().fit(X)

X_norm = scaler.transform(X)

#Train = 0 : 200 Test = 201 : 250

X_train = X_norm[:4288]

Y_train = Y[:4288]

X_test = X_norm [4289:]
Y_test = Y[4289:]

#DEFINING MODEL
from keras import regularizers

model = keras.Sequential([
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(128, activation = tf.nn.relu),
    keras.layers.Dense(1,activation = keras.activations.linear)
])

#MODEL COMPILATION
model.compile(optimizer=tf.train.AdamOptimizer(), metrics = ['root_mean_sqaured_error'], loss='root_mean_squared_error')

keras_callbacks = [keras.callbacks.EarlyStopping(monitor = 'root_mean_absolute_error', patience = 20, verbose = 0)]

model.fit(X_train, Y_train, epochs = 200, batch_size = 32)

#MODEL TRAINING RESULT
score_3 = model.evaluate(X_test, Y_test, verbose = 0)
print(score_3[1])


model.save('model3_v1.h5')