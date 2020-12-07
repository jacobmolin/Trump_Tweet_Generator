# Learn from a part of the data set (or a specific year) and predict a Trump tweet

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

data = pd.read_csv('data/tweets_11-06-2020.csv')
# print(data.head(10), '\n')

user_year = '2016'
df =data[(data["date"] >= user_year + '-01-01 00:00:00') & (data["date"] <= user_year + '-01-02 23:59:59')]

print('len(df):')
print(len(df))



# Delete re-tweets
df = df[~df.text.str.contains("RT")]
#print('df = df[~df.text.str.contains("RT")]')
#print(df.dtypes)

#print(df.iloc[0].isRetweet)
print(type(df.iloc[0].isRetweet))
# df = df[~df.isRetweet.str == 't']


df = df[~df.text.str.contains("RT")]
df = df[~df.text.str.contains("@")]
df = df[~df.text.str.contains("http")]
#print("After ~RT:", len(df))

df = df[~(df.isRetweet == "t")]
#print("After ~t:",len(df))

# TRY TO REMOVE ALL LEADING AND TRAILING WS
#df = df[~(df.text.str.strip())]

# REMOVE ROWS CONTAINING HTTP?
#df = df[~df.text.str.contains("http")]
# print("After ~http:",len(df))

#print(df.head(100), '\n')
# All tweets in one string
text = ''.join(df["text"])

text = text.lower()
print(text)

# all_tweets = all_tweets.replace('@', '')

# all_tweets = re.sub(r'http\S+', ' ', all_tweets)
# all_tweets = " ".join(all_tweets.split())

#Summarize months, user_month is chosen by user.
user_month = 1
# timeInterval = 1 / user_month
monthText = [user_month]

# for i in range(user_month):
#     if i < 10:
#         df = data[(data["date"] >= user_year + '-0' + i + '-01 00:00:00') & (data["date"] <= user_year + '-0' + i + '-30 23:59:59')]
        
#     else:
#         df = data[(data["date"] >= user_year + '-' + i + '-01 00:00:00') & (data["date"] <= user_year +  '-' + i + '-30 23:59:59')]

#     monthText[i] = ''.join(df["text"])
#     monthText[i] = monthText[i].lower()

# characters = sorted(list(set(text)))
# n_to_char = {n:char for n, char in enumerate(characters)}
# char_to_n = {char:n for n, char in enumerate(characters)}

# X = []
# Y = []
# length = len(monthText[0])
# print(length)
# seq_length = 100
# for i in range(0, length-seq_length, 1):
#     sequence = monthText[0][i:i + seq_length]
#     label =monthText[0][i + seq_length]
#     X.append([char_to_n[char] for char in sequence])
#     Y.append(char_to_n)

#creating character mappings
characters = sorted(list(set(text)))
print((set(text)))
n_to_char = {n:char for n, char in enumerate(characters)}
char_to_n = {char:n for n, char in enumerate(characters)}


# #Data pre-processing
X = []
Y = []
length = len(text)
seq_length = 100

for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label =text[i + seq_length]
    X.append([char_to_n[char] for char in sequence])
    Y.append(char_to_n[label])

X_modified = np.reshape(X, (len(X), seq_length, 1))
X_modified = X_modified / float(len(characters))
Y_modified = np_utils.to_categorical(Y)


# #A deeper model
model = Sequential()
model.add(LSTM(400, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(400, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(400))
model.add(Dropout(0.2))
model.add(Dense(Y_modified.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

# model.fit(X_modified, Y_modified, epochs=10, batch_size=10)

# model.save_weights('text_generator_400_0.2_400_0.2_400_0.2_100.h5')

model.load_weights('C:/Users/henke/Documents/GitHub/TNM108/Project/text_generator_400_0.2_400_0.2_400_0.2_100.h5')


# #Generating text
string_mapped = X[99]
full_string = [n_to_char[value] for value in string_mapped]
# generating characters
for i in range(400):
    x = np.reshape(string_mapped,(1,len(string_mapped), 1))
    x = x / float(len(characters))

    pred_index = np.argmax(model.predict(x, verbose=0))
    seq = [n_to_char[value] for value in string_mapped]
    full_string.append(n_to_char[pred_index])

    string_mapped.append(pred_index)
    string_mapped = string_mapped[1:len(string_mapped)]


#combining text
txt=""
for char in full_string:
    txt = txt+char
print(txt)