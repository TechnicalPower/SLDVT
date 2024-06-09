import os
import tensorflow
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Input
from keras.callbacks import TensorBoard
from keras.optimizers import Adam
import utils.action_parser as action_parser
import constants.configuration

# model_1 => Original
def model_build():
    model = Sequential()

    # LSTM layers
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(constants.configuration.ACTION_LIST), activation='softmax'))  # Output layer with softmax activation for classification

    return model

# model_2 => DukSung Women's University
def model_build_2():
    model = Sequential([
        Input(shape=(30, 1662), name='input_layer'),  
        LSTM(512, return_sequences=False, activation='relu', name='lstm_layer1'),  
        Dense(1024, activation='relu', name='dense_layer1'), 
        Dropout(0.3, name='dropout_layer'),  
        Dense(256, activation='relu', name='dense_layer2'),  
        Dense(256, activation='relu', name='dense_layer3'),  
        Dense(len(constants.configuration.ACTION_LIST), activation='softmax', name='output_layer')  
    ])
    return model


# model_3 => DukSung Women's University + tanh activation function for input layer
def model_build_3():
    model = Sequential([
        Input(shape=(30, 1662), name='input_layer'),  # 입력층 정의, M은 프레임당 특성 수
        LSTM(512, return_sequences=False, activation='tanh', name='lstm_layer1'),  
        Dense(1024, activation='relu', name='dense_layer1'),  # 첫 번째 Dense 층
        Dropout(0.3, name='dropout_layer'),  # 드롭아웃 적용, 과적합 방지
        Dense(256, activation='relu', name='dense_layer2'),  # 두 번째 Dense 층
        Dense(256, activation='relu', name='dense_layer3'),  # 세 번째 Dense 층
        Dense(len(constants.configuration.ACTION_LIST), activation='softmax', name='output_layer') 
    ])
    return model


# model_4 => Original + tanh activation function for input layer
def model_build_4():
    model = Sequential()

    # LSTM layers
    model.add(LSTM(64, return_sequences=True, activation='tanh', input_shape=(30,1662)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(constants.configuration.ACTION_LIST), activation='softmax')) 

    return model
    
    



def model_build_custom():

    action_list = action_parser.parse_actions("actions.txt")
    model = Sequential()

    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
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

    optimizer = Adam(clipvalue=0.5)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['categorical_accuracy'])

    model.fit(X_train, y_train, epochs=2000, callbacks=[tb_callback])
    
    return model

def learning_model_custom(X_train, y_train):
    log_dir = os.path.join('Logs')

    tb_callback = TensorBoard(log_dir)

    model = model_build_custom()


    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=200, callbacks=[tb_callback])
    
    return model







