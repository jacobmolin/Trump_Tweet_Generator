

# # Summarize months, user_month is chosen by user.
# user_month = 1
# # timeInterval = 1 / user_month
# monthText = [user_month]

# # for i in range(user_month):
# #     if i < 10:
# #         df = data[(data["date"] >= user_year + '-0' + i + '-01 00:00:00') & (data["date"] <= user_year + '-0' + i + '-30 23:59:59')]

# #     else:
# #         df = data[(data["date"] >= user_year + '-' + i + '-01 00:00:00') & (data["date"] <= user_year +  '-' + i + '-30 23:59:59')]

# #     monthText[i] = ''.join(df["text"])
# #     monthText[i] = monthText[i].lower()

# # characters = sorted(list(set(text)))
# # n_to_char = {n:char for n, char in enumerate(characters)}
# # char_to_n = {char:n for n, char in enumerate(characters)}

# # X = []
# # Y = []
# # length = len(monthText[0])
# # print(length)
# # seq_length = 100
# # for i in range(0, length-seq_length, 1):
# #     sequence = monthText[0][i:i + seq_length]
# #     label =monthText[0][i + seq_length]
# #     X.append([char_to_n[char] for char in sequence])
# #     Y.append(char_to_n)

# # creating character mappings
# characters = sorted(list(set(text)))
# print((set(text)))
# n_to_char = {n: char for n, char in enumerate(characters)}
# char_to_n = {char: n for n, char in enumerate(characters)}


# # #Data pre-processing
# X = []
# Y = []
# length = len(text)
# seq_length = 100

# for i in range(0, length-seq_length, 1):
#     sequence = text[i:i + seq_length]
#     label = text[i + seq_length]
#     X.append([char_to_n[char] for char in sequence])
#     Y.append(char_to_n[label])

# X_modified = np.reshape(X, (len(X), seq_length, 1))
# X_modified = X_modified / float(len(characters))
# Y_modified = np_utils.to_categorical(Y)


# # #A deeper model
# model = Sequential()
# model.add(LSTM(400, input_shape=(
#     X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(400, return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(400))
# model.add(Dropout(0.2))
# model.add(Dense(Y_modified.shape[1], activation='softmax'))

# model.compile(loss='categorical_crossentropy', optimizer='adam')

# # Train model
# # model.fit(X_modified, Y_modified, epochs=10, batch_size=10)
# # model.save_weights('text_generator_400_0.2_400_0.2_400_0.2_100.h5')

# model.load_weights('/text_generator_400_0.2_400_0.2_400_0.2_100.h5')


# # Generating text
# string_mapped = X[99]
# full_string = [n_to_char[value] for value in string_mapped]
# # generating characters
# for i in range(400):
#     x = np.reshape(string_mapped, (1, len(string_mapped), 1))
#     x = x / float(len(characters))

#     pred_index = np.argmax(model.predict(x, verbose=0))
#     seq = [n_to_char[value] for value in string_mapped]
#     full_string.append(n_to_char[pred_index])

#     string_mapped.append(pred_index)
#     string_mapped = string_mapped[1:len(string_mapped)]


# # Combining text
# txt = ""
# for char in full_string:
#     txt = txt+char
# print(txt)
