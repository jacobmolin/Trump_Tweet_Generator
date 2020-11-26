import pandas as pd

userInput = 0
data = pd.read_csv('data/tweets_11-06-2020.csv')
# print(data.head(5))
# print(type(data))
# print(type(data['date'].shape))
# print(data[(data["date"] >= '2012-01-03 00:00:00')
#    & (data["date"] <= '2012-01-06 23:59:59')])


data_2012 = data[(data["date"] >= {userInput}+'-01-01 00:00:00')
                 & (data["date"] <= '2012-12-31 23:59:59')]

print(data_2012)
