##### $$$$$ To calculate the sentiment polarities of a stock financial news/tweets $$$$$ #####


from textblob import TextBlob
import numpy as np
import pandas as pd


df = pd.read_csv("Combined_News_DJIA.csv") # change dataset according to stock

# Preprocessing

df.TimeStamp = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df.index = df.TimeStamp
df = df.drop(['Date', 'Label'], axis =1)


df = df['2008-08-08':'2016-07-01']   # Select timeframe according to need


# some more preprocessing
idx = pd.date_range('08-08-2008', '01-07-2016')
df = df.reindex(idx, fill_value="a")


print(df)
print(df.shape)


sentiment_scores = np.empty([2885,25], dtype=float)

for i in range (0, 2885):
    for j in range(0,25):
        sentiment_scores[i][j] = TextBlob(df.iloc[i][j]).sentiment.polarity

sent = pd.DataFrame(sentiment_scores, index = df.index)
sent['mean'] = sent.mean(axis = 1)
sent.to_csv("sent.csv", index = False)
