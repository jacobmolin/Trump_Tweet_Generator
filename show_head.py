import pandas as pd


data = pd.read_csv('data/tweets_11-06-2020.csv')

user_year = '2016'
df = data[(data["date"] >= user_year + '-01-01 00:00:00') &
          (data["date"] <= user_year + '-12-31 23:59:59')]

print(df.head())
print('length df:', len(data))
