import os
import tensorflow
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense 
from keras.callbacks import TensorBoard
import constants

def model_build():
    model = Sequential()

    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(len(constants.ACTION_LIST), activation='softmax'))
    return model


def learning_model(X_train, y_train, res):
    log_dir = os.path.join('Logs')

    tb_callback = TensorBoard(log_dir)

    model = model_build()


    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

    model.fit(X_train, y_train, epochs=200, callbacks=[tb_callback])
    
    return model








