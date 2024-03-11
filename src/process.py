from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

import constants
import numpy as np
import os
import LSTM_model


def process():
    label_map = {label: num for num, label in enumerate(np.array(constants.ACTION_LIST))}

    sequences, labels = [], []
    for action in np.array(constants.ACTION_LIST):
        for sequence in range(constants.NP_SEQUENCE):
            window = []
            for frame_num in range(constants.NP_LENGTH):
                res = np.load(os.path.join(constants.DATA_PATH_STRING, action, str(sequence), "{}.npy".format(frame_num)))
                window.append(res)
            sequences.append(window)
            labels.append(label_map[action])
    X = np.array(sequences)
    y = to_categorical(labels).astype(int)
    res = [.7, 0.2, 0.1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

    model = LSTM_model.learning_model(X_train, y_train)

    res = model.predict(X_test)
    model.save('action.keras')

def load():
    model = LSTM_model.model_build()
    model.load_weights('action.keras')
    return model




# Only for testing purpose
if __name__ == "__main__":
    process()