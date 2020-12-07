# Learn from a part of the data set (or a specific year) and predict a Trump tweet

import numpy as np
import pandas as pd
import re

# data = pd.read_csv('data/tweets_11-06-2020.csv')

# user_year = '2016'
# df = data[(data["date"] >= user_year + '-01-01 00:00:00') &
#           (data["date"] <= user_year + '-12-31 23:59:59')]

# print('len(df):')
# print(len(df))


def cleanup(df):
    # Remove all rows that are retweets
    df = df[~(df.isRetweet == "t")]

    # Delete re-tweets
    # df = df[~df.text.str.contains("RT")]
    # print('df = df[~df.text.str.contains("RT")]')
    # print(df.dtypes)

    # print(df.iloc[0].isRetweet)
    # print(type(df.iloc[0].isRetweet))

    # All tweets in one string
    text = ''.join(df["text"])

    # Remove all links on tweets
    text = re.sub(r'http\S+', ' ', text)

    # Put space before @
    text = text.replace('@', ' @')

    # Replace &amp
    text = text.replace('&amp', '&')

    # Replace #
    text = text.replace('#', ' #')

    replacement = [',', '.', '!', '\"', ':',
                   '?', '(', ')', '’', '“', '‘', '~', '-', '—', '/', '”', '–']
    for r in replacement:
        text = text.replace(r, ' ')

    # Lower capital letters to get fewer unique words
    text = text.lower()

    # print(text)
    return text
    # print(len(text.split(' ')))
    # print(text.split(' '))
