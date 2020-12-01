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



tweet_split = all_tweets.split('""')


formatTweet = ''
# @@TODO: CLEAN UP: delete everything such as "http..." and "(cont)"
# All unique tweets from Trump are quoted, while retweets start with RT: , and links [only] starts with http(s)://....
for i in tweet_split:
    if( 'RT' not in i or 'http' not in i or '@' not in i):
        formatTweet = formatTweet + i


formatTweet = formatTweet.replace('@', '')
formatTweet = formatTweet.replace('(cont)', '')
formatTweet = formatTweet.replace('RT', '')
formatTweet = formatTweet.strip('http')
formatTweet = formatTweet.strip('???')

#Remove http from string
import re
formatTweet = re.sub(r'http\S+', '', formatTweet)



print(summarize(formatTweet, words=100))
#print(sumis)
#print(sumis.replace('@', ''))