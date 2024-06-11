import os
import tensorflow
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense 
from keras.callbacks import TensorBoard
import utils.action_parser as action_parser
import constants.configuration 

def model_build():
    model = Sequential()

    # LSTM layers
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,constants.configuration.TOTAL_LANDMARK)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(constants.configuration.ACTION_LIST), activation='softmax'))  # Output layer with softmax activation for classification

    return model



def model_build_custom():

    action_list = action_parser.parse_actions("actions.txt")
    model = Sequential()

    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,constants.configuration.TOTAL_LANDMARK)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(len(action_list), activation='softmax'))
    return model

def learning_model(X_train, y_train):
    log_dir = os.path.join('Logs')

    tb_callback = TensorBoard(log_dir)

    model = model_build()


    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

    model.fit(X_train, y_train, epochs=10000, callbacks=[tb_callback])
    
    return model

def learning_model_custom(X_train, y_train):
    log_dir = os.path.join('Logs')

    tb_callback = TensorBoard(log_dir)

    model = model_build_custom()


    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=200, callbacks=[tb_callback])
    
    return model







