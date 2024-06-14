import os
import constants.configuration as configuration
import numpy as np

# !! DATA path to store the folder to detect
DATA_PATH = os.path.join(configuration.DATA_PATH_STRING)
DATA_PATH_CUSTOM = os.path.join(configuration.DATA_PATH_CUSTOM)

# For testing purpose with fixed number of dataset
## Following words:
### 1. Hello
### 2. Thanks
### 3. ILoveYou
actions = np.array(configuration.ACTION_LIST)


### REFRENCE FROM constants.py
np_sequence = configuration.NP_SEQUENCE



np_constant = configuration.NP_LENGTH

def main():

    for action in actions:
        for sequence in range(np_sequence):
            try:
                os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
            except:
                print("DATA GENERATION FAILED")
                pass

def custom_flow_data_generate(word):

    for sequence in range(np_sequence):
        try:
            os.makedirs(os.path.join(DATA_PATH_CUSTOM, word, str(sequence)))
        except:
            print("CUSTOM FLOW: DATA GENERATION FAILED")
            pass

    

if __name__ == "__main__":
    main()
