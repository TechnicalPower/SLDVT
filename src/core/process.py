# Splitting the dataset into training and test sets
from sklearn.model_selection import train_test_split
#Converting integer labels into one-hot encoding
from tensorflow.keras.utils import to_categorical

# Import necessary modules and files
import os
import sys
sys.path.append("..")

import core.LSTM_model as LSTM_model
import utils.action_parser as action_parser
import constants.configuration as configuration
import numpy as np
def process():
    # Create a label map to map action labels to numerical values(index of action in ACTION_LIST)
    label_map = {label: num for num, label in enumerate(configuration.ACTION_LIST)}
    
    # sequece : list that store sequence of each frame for the each action
    # labels: list that store sequece of trained action labels 
    sequences, labels = [], []
    # Iterate over each action in the ACTION_LIST
    for action in configuration.ACTION_LIST:
        # Generate sequences for each action 
        for sequence in range(configuration.NP_SEQUENCE):
            # window : list that store frames composing each sequence
            window = []
            # Load frames for each sequence
            for frame_num in range(configuration.NP_LENGTH):
                # Load each frame that stores after the training
                res = np.load(os.path.join(configuration.DATA_PATH_STRING, action, str(sequence), "{}.npy".format(frame_num)))
                # append to the window list (it will store all the frames for each action)
                window.append(res)
            
            # store list of all the frames for each sequence
            sequences.append(window)
            # store the order of trained action labels
            labels.append(label_map[action])
    #convert sequeces to numpy array
    X = np.array(sequences)
    # convert labels to the one-hot encoding 
    y = to_categorical(labels, num_classes=len(configuration.ACTION_LIST)).astype(int)
    
    # Split data into train and test sets, 0.05% of data will be used for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

    # Train the LSTM model
    model = LSTM_model.learning_model(X_train, y_train)

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)

    # Get predictions on test data
    predictions = model.predict(X_test)

    # Save the trained model (trained parameter)
    model.save_weights('../model/action.keras')

    # save the model 
    model.save('my_model')

    return loss, accuracy, predictions

# Function to process data for custom flow
def process_custom_flow():
    # Parse action list from a file
    action_list = np.array(action_parser.parse_actions("actions.txt"))
    # Create a label map to map action labels to numerical values(index of action in action_list)
    label_map = {label: num for num, label in enumerate(action_list)}

    # sequece : list that store sequence of each frame for the each action
    # labels: list that store sequece of trained action labels
    sequences, labels = [], []
    
    # Iterate over each action in the custom action list
    for action in action_list:
        # Generate sequences for each action
        for sequence in range(configuration.NP_SEQUENCE):
            # window : list that store frames composing each sequence
            window = []
            # Load frames for each sequence
            for frame_num in range(configuration.NP_LENGTH):
                # Load each frame that stores after the training
                res = np.load(os.path.join(configuration.DATA_PATH_CUSTOM, action, str(sequence), "{}.npy".format(frame_num)))
                # append to the window list (it will store all the frames for each action)
                window.append(res)
                
            # store list of all the frames for each sequence
            sequences.append(window)
            # store the order of trained action labels
            labels.append(label_map[action])
    #convert sequeces to numpy array
    X = np.array(sequences)
    # convert labels to the one-hot encoding 
    y = to_categorical(labels).astype(int)

    # Split data into train and test sets, 0.05% of data will be used for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

    # Train the LSTM model with custom data
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

# Function to load the default model
def load():
    # Get the path to the default model
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_path, '../model/action.keras')

    # Build the model architecture
    model = LSTM_model.model_build()
    # Load weights of the pre-trained model
    model.load_weights(model_path)
    return model

# Function to load the custom model
def load_custom_flow():
    # Build the model architecture for custom flow
    model = LSTM_model.model_build_custom()
    # Load weights of the custom-trained model
    model.load_weights('action_custom.keras')
    return model

# Main function to execute for testing purpose
if __name__ == "__main__":
    process()
