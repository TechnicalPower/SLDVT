import os
import tensorflow
from keras.models import Sequential
from keras.layers import LSTM, Dense 
from keras.callbacks import TensorBoard
import constants

log_dir = os.path.join('Logs')


tb_callback = TensorBoard(log_dir)

model = Sequential()

model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))

model.add(Dense(constants.ACTION_LIST.length, activation='softmax'))


