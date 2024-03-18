from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

import constants
import numpy as np
import os
import LSTM_model
import action_parser


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

def process_custom_flow():
    action_list = np.array(action_parser.parse_actions("actions.txt"))
    label_map = {label: num for num, label in enumerate(action_list)}

    sequences, labels = [], []
    for action in action_list:
        for sequence in range(constants.NP_SEQUENCE):
            window = []
            for frame_num in range(constants.NP_LENGTH):
                res = np.load(os.path.join(constants.DATA_PATH_CUSTOM, action, str(sequence), "{}.npy".format(frame_num)))
                window.append(res)
            sequences.append(window)
            labels.append(label_map[action])
    X = np.array(sequences)
    y = to_categorical(labels).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

    model = LSTM_model.learning_model_custom(X_train, y_train)

    # Get predictions on test data
    res = model.predict(X_test)

    # Option 1: Compute evaluation metrics
    evaluation_metrics = model.evaluate(X_test, y_test)
    print("Evaluation Metrics:", evaluation_metrics)

    # Option 2: Save predictions to a file
    np.savetxt('predictions.txt', res)

    # Option 3: Do something else with the predictions as needed

    # Save the trained model
    model.save('action_custom.keras')

def load():
    model = LSTM_model.model_build()
    model.load_weights('action.keras')
    return model
def load_custom_flow():
    model = LSTM_model.model_build_custom()
    model.load_weights('action_custom.keras')
    return model




# Only for testing purpose
if __name__ == "__main__":
    process_custom_flow()