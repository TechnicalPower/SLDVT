import os
import tensorflow
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, BatchNormalization
from keras.callbacks import TensorBoard
import utils.action_parser as action_parser
import constants.configuration
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers

def model_build():
    model = Sequential()

    # LSTM layers with Batch Normalization
    model.add(LSTM(128, return_sequences=True, activation='relu', input_shape=(30, 1662)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    
    model.add(LSTM(256, return_sequences=True, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    
    model.add(LSTM(128, return_sequences=False, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    
    # Fully connected layers with L2 regularization
    model.add(Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(len(constants.configuration.ACTION_LIST), activation='softmax'))  # Output layer with softmax activation for classification

    return model



def model_build_custom():

    action_list = action_parser.parse_actions("actions.txt")
    model = Sequential()

    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(action_list), activation='softmax'))
    return model

def learning_model(X_train, y_train):
    log_dir = os.path.join('Logs')

    tb_callback = TensorBoard(log_dir)

    model = model_build()

    optimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['categorical_accuracy'])

    model.fit(X_train, y_train, epochs=100, callbacks=[tb_callback])
    
    return model

def learning_model_custom(X_train, y_train):
    log_dir = os.path.join('Logs')

    tb_callback = TensorBoard(log_dir)

    model = model_build_custom()


    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=200, callbacks=[tb_callback])
    
    return model







