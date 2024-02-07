# !! STORE CONSTANT VALUE IN THIS FILE FOR BEST PRACTICE

# used by data_generate.py --
ACTION_LIST = [
    "Hello",
    "Thanks",
    "Iloveyou"
] ## Following array store the list of action to detect
NP_SEQUENCE = 30 ## Number of folders on the action
NP_LENGTH = 30 ## Number of frames on single sequence (folder)
DATA_PATH_STRING = 'dataset' ## DATA PATH

# used by mcapture.py --
MIN_DETECTION_CONFIDENCE = 0.5 ## confidence rate - hyperparameter for media pipe for detection inital action
MIN_TRACKING_CONFIDENCE = 0.5 ## confidence rate - hyperparameter for media pipe for detection tracking action
SIZE_POSE_LANDMARK = 132 ## constants of len >> pose_landmarks
SIZE_FACE_LANDMARK = 1404 ## constants of len >> face_landmarks
SIZE_LEFT_HAND_LANDMARK = 63 ## constants of len >> left_hand_landmarks
SIZE_RIGHT_HAND_LANDMARK = 63 ## constants of len >> right_hand_landmarks
NAME_FRAME = 'Motion Capture' ## name of frame 
KILL_PROCESS_KEY_INPUT = 'q' ## kill process key !!

