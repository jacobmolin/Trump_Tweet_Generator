
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils


def modelling(model, X_modified, Y_modified):
    model.add(LSTM(700, input_shape=(
        X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(700, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(700))
    model.add(Dropout(0.2))
    model.add(Dense(Y_modified.shape[1], activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')

    model.fit(X_modified, Y_modified, epochs=3, batch_size=100)

    model.save_weights(
        'models/text_generator_gigant_700_0.2_700_0.2_700_0.2_20.h5')

    return model
