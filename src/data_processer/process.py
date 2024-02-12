from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import data_generate
import constants
import numpy as np
import os
label_map = {label: num for num, label in enumerate(data_generate.actions)}

sequences, labels = [], []
for action in data_generate.actions:
    for sequence in range(constants.NP_SEQUENCE):
        window = []
        for frame_num in range(constants.NP_LENGTH):
            res = np.load(os.path.join(data_generate.DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])
