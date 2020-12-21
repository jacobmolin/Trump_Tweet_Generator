import pandas as pd

print('\n')
data = pd.read_csv('data/tweets_11-06-2020.csv')

user_year = '2016'
df = data[(data["date"] >= user_year + '-03-01 00:00:00') &
          (data["date"] <= user_year + '-03-31 23:59:59')]

print(df.head(15))
print('\nlength df:', len(data))
print('\n')
