# !! STORE CONSTANT VALUE IN THIS FILE FOR BEST PRACTICE
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

# used by data_generate.py --
ACTION_LIST = [
    "again",
    "also",
    "ask",
    "can",
    "come",
    "deaf",
    "friend",
    "have",
    "I",
    "internet",
    "like",
    "my",
    "remember",
    "sign word",
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
SIZE_FACE_LANDMARK = 294    ## constants of len >> face_landmarks
SIZE_LEFT_HAND_LANDMARK = 63 ## constants of len >> left_hand_landmarks
SIZE_RIGHT_HAND_LANDMARK = 63 ## constants of len >> right_hand_landmarks
NAME_FRAME = 'Motion Capture' ## name of frame 
KILL_PROCESS_KEY_INPUT = 'q' ## kill process key !!

FACE_OVAL = mp_face_mesh.FACEMESH_FACE_OVAL

FACE_LIPS = frozenset({(78, 191), (191, 80), (80, 81), (81, 82), (82, 13), (13, 312),
               (312, 311), (311, 310), (310, 415), (415, 308), (308,324), 
               (324, 318), (318, 402), (402, 317), (317, 14), (14, 87), (87, 178), 
               (178, 88), (88, 95), (95, 78)})

RIGHT_EYE = frozenset({(33, 246), (246, 161), (161, 160), (160, 159), (159, 158), (158, 157), (157, 173),
               (173, 133), (133, 155), (155, 154), (154, 153), (153, 145), (145, 144), (144, 163), 
               (163, 7), (7, 33)})

LEFT_EYE  = frozenset({(362, 398), (398, 384), (384, 385), (385, 386), (386, 387), (387, 388), (388, 466),
               (466, 263), (263, 249), (249, 390), (390, 373), (373, 374), (374, 380), (380, 381), 
               (381, 382), (382, 362)})

RIGHT_EYEBROW = frozenset({(46, 53), (53, 52), (52, 65), (65, 55)})

LEFT_EYEBROW = frozenset({(285, 295), (295, 282), (282, 283), (283, 276)})

EYEBROW_LANDMARK = 5

TOTAL_LANDMARK = 552

# FLOW VARIABLES --
FLOW_CUSTOM = "C"
FLOW_LEARNING = "L"


# used by voice_translate.py --
INPUT_TEST_DIRECTORY = "../test/input/input.txt"
