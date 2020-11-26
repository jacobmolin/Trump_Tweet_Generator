# check sentiment for a certain week or other period
# worst/best period of the year
# most talked about topic of the year
# do analysis
# think about other dimensions during the way
# start with yearly

import pandas as pd
from summa.summarizer import summarize
from summa import keywords

print('-----WELCOME TO TRUMP TWEET BANK-----')
print('- See a year through the eyes of Trump\'s Twitter feed! -\n')
# user_year = input('Enter a year to summarize: ')
user_year = '2012'
print(f'user_year = {user_year}\n')

data = pd.read_csv('data/tweets_11-06-2020.csv')
# print(data.head(1), '\n')
# print(type(data))
# print(type(data['date'].shape))
# print(data[(data["date"] >= '2012-01-03 00:00:00')
#    & (data["date"] <= '2012-01-06 23:59:59')])


user_selected_data = data[(data["date"] >= user_year + '-01-01 00:00:00')
                          & (data["date"] <= user_year + '-01-10 23:59:59')]
# print(user_selected_data)
# User_Selected_data is a matrix with 9xn elements. To summarize the text we concatenate the chosen user input.

# print(type(user_selected_data))
# all_tweets = user_selected_data.sum(axis=2).astype(int).astype(str)
all_tweets = ' '.join(user_selected_data["text"])
# print('all_tweets: ', type(all_tweets))

# CLEAN UP: delete everything such as "http..." and "(cont)"

# Might have to concatenate the text and then find the text in the dataframe to be able to see more information about the tweet, such as date, device and retweets.
# Like This:
# df[(df == n_input).any(1)].stack()[lambda x: x != n_input].unique()
# {df is our dataframe, AKA user_selected_input.}


# print(summarize(all_tweets, ratio=0.2))
print(summarize(all_tweets, words=100))
