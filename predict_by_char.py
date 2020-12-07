# Learn from a part of the data set (or a specific year) and predict a Trump tweet

from cleanup import cleanup_text
from cleanup import cleanup_tweets
from cleanup import cleanup_for_char
from modelling import modelling
import numpy as np
import pandas as pd
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

# ---- For running on GPU ----
import tensorflow as tf
config = tf.compat.v1.ConfigProto(gpu_options=tf.compat.v1.GPUOptions(
    per_process_gpu_memory_fraction=0.8)
    # device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)
# ----------------------------

# Load data set
data = pd.read_csv('data/tweets_11-06-2020.csv')

user_year = '2016'
df = data[(data["date"] >= user_year + '-01-01 00:00:00') &
          (data["date"] <= user_year + '-01-31 23:59:59')]

print('length df:', len(df))

tweet_list = cleanup_tweets(df)
print('length tweet_list:', len(tweet_list))

text = cleanup_for_char(' '.join(tweet_list))
# print(text)

# Words
words = text.split()
words_unique = sorted(list(set(words)))
print('length words:', len(words))
print('length words_unique:', len(words_unique))

# Creating char mapping
characters = sorted(list(set(text)))
n_to_char = {n: char for n, char in enumerate(characters)}
char_to_n = {char: n for n, char in enumerate(characters)}
# print(characters)
print('length unique characters:', len(characters))
# print('n_to_char: ', n_to_char)
# print('char_to_n: ', char_to_n)

# Data pre-processing
X_train = []
Y_target = []
length = len(text)
print('length text:', length)
seq_length = 100

for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label = text[i + seq_length]
    X_train.append([char_to_n[char] for char in sequence])
    Y_target.append(char_to_n[label])

print('len(X_train):', len(X_train))

# We need to transform the array Y into a one-hot encoded format.
X_modified = np.reshape(X_train, (len(X_train), seq_length, 1))
X_modified = X_modified / float(len(characters))
Y_modified = np_utils.to_categorical(Y_target)

run_model_fit = True

[model, filename] = modelling(X_modified, Y_modified, run_model_fit)

if filename != '':
    model.load_weights(filename)
else:
    model.load_weights('models/text_generator_400_0.2_400_0.2_e1_bs100.h5')

string_mapped = X_train[99]
full_string = [n_to_char[value] for value in string_mapped]
# generating characters
for i in range(400):
    x = np.reshape(string_mapped, (1, len(string_mapped), 1))
    x = x / float(len(characters))

    pred_index = np.argmax(model.predict(x, verbose=0))
    seq = [n_to_char[value] for value in string_mapped]
    full_string.append(n_to_char[pred_index])

    string_mapped.append(pred_index)
    string_mapped = string_mapped[1:len(string_mapped)]

# combining text
txt = ""
for char in full_string:
    txt = txt + char
print('txt:', txt)
