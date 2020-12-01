# check sentiment for a certain week or other period
# worst/best period of the year
# most talked about topic of the year
# do analysis
# think about other dimensions during the way
# start with yearly
# Things to compare : 
# - Most frequent used word?
# - How many retweets does he do in comparisson with 'regular'
# - Predict a "Trump Tweet?"
# - Trump tweet neg/pos?
# - Summarize each :-) month and then do a summarization of 12 months? -> Make predictions of the upcoming month.
# - What will Trump say next week?


import re
import pandas as pd
from summa.summarizer import summarize
from summa import keywords

print('-----WELCOME TO TRUMP TWEET BANK-----')
print('- See a year through the eyes of Trump\'s Twitter feed! -\n')
# user_year = input('Enter a year to summarize: ')
user_year = '2016'
print(f'user_year = {user_year}\n')

data = pd.read_csv('data/tweets_11-06-2020.csv')
print(data.head(10), '\n')
# print(type(data))
# print(type(data['date'].shape))

user_selected_data = data[(data["date"] >= user_year + '-01-01 00:00:00') & (data["date"] <= user_year + '-03-30 23:59:59')]



# User_Selected_data is a matrix with 9xn elements. To summarize the text we concatenate the chosen user input.
# all_tweets = user_selected_data[user_selected_data['text'].contains('RT')]

print(len(user_selected_data))
user_selected_data = user_selected_data[~user_selected_data.text.str.contains("RT")]
print(len(user_selected_data))
all_tweets = ''.join(user_selected_data["text"])

# k = all_tweets.split('""')

# l = 0
# j = []
# for a in k:
#     if(not ((a[0]+a[1]) == 'RT')):
#         j[l] = a
#         l = l+1

# print(j)

# print(all_tweets)

# formatTweet = formatTweet.replace(' @', ' ')
# formatTweet = formatTweet.replace(' (cont) ', ' ')
# formatTweet = formatTweet.replace(' RT ', ' ')

to_remove = ['@']  # '(cont)'
# print(type(all_tweets))

for rem in to_remove:
    all_tweets = all_tweets.replace(rem, '')

all_tweets = re.sub(r'http\S+', ' ', all_tweets)
all_tweets = " ".join(all_tweets.split())

print('TWEET SUMM')
all_tweets = (summarize(all_tweets, words=150))

# all_tweets = all_tweets.replace('""', '\n\n')
print(all_tweets)

# @@TODO: CLEAN UP: delete everything such as "http..." and "(cont)"
# All unique tweets from Trump are quoted, while retweets start with RT: , and links [only] starts with http(s)://....
