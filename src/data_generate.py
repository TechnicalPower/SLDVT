import os
import constants
import numpy as np

# !! DATA path to store the folder to detect
DATA_PATH = os.path.join(constants.DATA_PATH_STRING)

actions = np.array(constants.ACTION_LIST)

np_sequence = constants.NP_SEQUENCE

np_constant = constants.NP_LENGTH

def main():

    for action in actions:
        for sequence in range(np_sequence):
            try:
                os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
            except:
                print("DATA GENERATION FAILED")
                pass

if __name__ == "__main__":
    main()