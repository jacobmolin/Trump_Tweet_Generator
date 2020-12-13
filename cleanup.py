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


def cleanup_text(text):
    # Remove all rows that are retweets
    # df = df[~(df.isRetweet == "t")]

    # Remove all rows that are answers to tweets
    # df = df[~(df.text.str.contains('"""'))]

    # Delete re-tweets
    # df = df[~df.text.str.contains("RT")]
    # print('df = df[~df.text.str.contains("RT")]')
    # print(df.dtypes)

    # print(df.iloc[0].isRetweet)
    # print(type(df.iloc[0].isRetweet))

    # All tweets in one string
    # text = ''.join(df["text"])

    # Remove all links on tweets
    # text = re.sub(r'http\S+', ' ', text)

    # Put space before @
    # text = text.replace('@', ' @')

    # Replace &amp
    # text = text.replace('&amp', '&')

    # Replace #
    # text = text.replace('#', ' #')

    replacement = [',', '.', '!', '\"', ':',
                   '?', '(', ')', '’', '“', '‘', '~', '-', '—', '/', '”', '–']
    # ['\"', '“', '~', '-', '\\', '/', '”']
    for r in replacement:
        text = text.replace(r, f' {r} ')

    # Remove multiple whitespaces
    # text = ' '.join(text.split())

    # Lower capital letters to get fewer unique words
    text = text.lower()

    # print(text)
    return text
    # print(len(text.split(' ')))
    # print(text.split(' '))


def cleanup_for_char(text):
    # Remove all rows that are retweets
    # df = df[~(df.isRetweet == "t")]

    # Remove all rows that are answers to tweets
    # df = df[~(df.text.str.contains('"""'))]

    # Delete re-tweets
    # df = df[~df.text.str.contains("RT")]
    # print('df = df[~df.text.str.contains("RT")]')
    # print(df.dtypes)

    # print(df.iloc[0].isRetweet)
    # print(type(df.iloc[0].isRetweet))

    # All tweets in one string
    # text = ''.join(df["text"])

    # Remove all links on tweets
    # text = re.sub(r'http\S+', ' ', text)

    # Put space before @
    # text = text.replace('@', ' @')

    # Replace &amp
    # text = text.replace('&amp', '&')

    # Replace #
    # text = text.replace('#', ' #')

    # replacement = [',', '.', '!', '\"', ':',
    #                '?', '(', ')', '’', '“', '‘', '~', '-', '—', '/', '”', '–']
    # ['\"', '“', '~', '-', '\\', '/', '”']
    replacement = ['-', '(1/2)', '(2/2)']
    for r in replacement:
        text = text.replace(r, ' ')

    # Remove multiple whitespaces
    text = ' '.join(text.split())

    # Lower capital letters to get fewer unique words
    text = text.lower()

    # print(text)
    return text
    # print(len(text.split(' ')))
    # print(text.split(' '))


def cleanup_tweets(df):

    # Remove all rows that are retweets
    df = df[~(df.isRetweet == "t")]

    # Remove all rows that are answers to tweets
    df = df[~(df.text.str.contains('"""'))]

    text_list = df.text.tolist()

    for i in range(len(text_list)):
        if '".' in text_list[i]:
            text_list[i] = text_list[i].replace('".', '')
            text_list[i] = text_list[i][0:len(text_list[i])-1]
            # print(text_list[i][len(text_list[i])-1])

        # Remove all links on tweets
        text_list[i] = re.sub(r'http\S+', ' ', text_list[i])

        # Put space before @
        text_list[i] = text_list[i].replace('.@', ' @')

        # Put space before @
        text_list[i] = text_list[i].replace('@', ' @')

        # Replace &amp
        text_list[i] = text_list[i].replace('&amp,', '&')

        # Replace &amp
        text_list[i] = text_list[i].replace('&amp;', '&')

        # Replace #
        text_list[i] = text_list[i].replace('#', ' #')

        # Replace ""
        text_list[i] = text_list[i].replace('""', '"')

        # Replace .
        # text_list[i] = text_list[i].replace('.', '. ')

        # replacement = ['\"', '“', '~', '-', '\\', '/', '”']  # '’', '‘',
        # for r in replacement:
        #     text_list[i] = text_list[i].replace(r, ' ')

        text_list[i] = ' '.join(text_list[i].split())

        # Lower capital letters to get fewer unique words
        # text_list[i] = text_list[i].lower()

    return text_list
