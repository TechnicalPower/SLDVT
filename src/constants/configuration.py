# !! STORE CONSTANT VALUE IN THIS FILE FOR BEST PRACTICE

# used by data_generate.py --
ACTION_LIST = [
    # "again",
    # "also",
    # "ask",
    # "bad",
    # "boy",
    # "but",
    "can",
    # "come",
    # "deaf",
    # "drink",
    # "drive",
    "eat",
    # "email",
    # "execute",
    # "family",
    # "feeling",
    # "few",
    # "find",
    # "fine",
    # "fingerspell",
    # "finish",
    # "for",
    # "forget",
    # "friend",
    # "get",
    # "girl",
    # "give",
    # "go",
    # "good",
    # "have",
    # "help",
    # "home",
    # "how",
    "I",
    # "internet",
    # "later",
    # "like",
    # "little",
    # "man",
    # "many",
    # "meet",
    # "more",
    # "my",
    # "name",
    # "need",
    # "new",
    # "now",
    # "please",
    # "remember",
    # "sign word",
]
## Following array store the list of action to detect for only testing purpose (Acutal use flow will not use this constant!)
NP_SEQUENCE = 30 ## Number of folders on the action
NP_LENGTH = 30 ## Number of frames on single sequence (folder)
DATA_PATH_STRING = '../dataset/Dataset-Mhia' ## DATA PATH
DATA_PATH_CUSTOM = 'dataset'

# used by mcapture.py --
MIN_DETECTION_CONFIDENCE = 0.5 ## confidence rate - hyperparameter for media pipe for detection inital action
MIN_TRACKING_CONFIDENCE = 0.5 ## confidence rate - hyperparameter for media pipe for detection tracking action
SIZE_POSE_LANDMARK = 132 ## constants of len >> pose_landmarks
SIZE_FACE_LANDMARK = 1404 ## constants of len >> face_landmarks
SIZE_LEFT_HAND_LANDMARK = 63 ## constants of len >> left_hand_landmarks
SIZE_RIGHT_HAND_LANDMARK = 63 ## constants of len >> right_hand_landmarks
NAME_FRAME = 'Motion Capture' ## name of frame 
KILL_PROCESS_KEY_INPUT = 'q' ## kill process key !!

# FLOW VARIABLES --
FLOW_CUSTOM = "C"
FLOW_LEARNING = "L"


# used by voice_translate.py --
INPUT_TEST_DIRECTORY = "../test/input/input.txt"

