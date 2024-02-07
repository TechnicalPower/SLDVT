import cv2
import numpy as np
import os 
from matplotlib import pyplot
import time
import mediapipe
import constants
#holistic model for image detection taking landmarks
mp_holistic = mediapipe.solutions.holistic

#image drawing on the frame model
mp_drawing = mediapipe.solutions.drawing_utils

def mediapipe_detection(img, model):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img.flags.writeable = False
    results = model.process(img)
    img.flags.writeable = True
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img, results

def draw_landmarks(img, results):
    mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
    mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

def extract_key_values(results):
    pose = []
    for res in results.pose_landmarks.landmark:
        test = np.array([res.x, res.y, res.z, res.visibility])
        pose.append(test)
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(constants.SIZE_POSE_LANDMARK)
    face = np.array([[res.x, res.y, res.z, res.visibility] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(constants.SIZE_FACE_LANDMARK)
    left_hand = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(constants.SIZE_LEFT_HAND_LANDMARK)
    right_hand = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(constants.SIZE_RIGHT_HAND_LANDMARK)
    return np.concatenate([pose, face, left_hand, right_hand])
def main():
    # VideoCapture with input 0 will call the camera to get motion captured
    # Reference: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#ae82ac8efcff2c5c96be47c060754a518
    cap = cv2.VideoCapture(0)

    # Returns true if video capturing has been initialized already
    with mp_holistic.Holistic(min_detection_confidence=constants.MIN_DETECTION_CONFIDENCE,
                               min_tracking_confidence=constants.MIN_TRACKING_CONFIDENCE) as holistic:
        while cap.isOpened():
            # Grabs, decodes and returns the next video frame
            # ret :
            # frame : 
            ret, frame = cap.read()
            img, results = mediapipe_detection(frame,holistic)
            draw_landmarks(img, results)
            cv2.imshow(constants.NAME_FRAME, img)
            print(results)
            #break for frame closure with typing 'q'
            if cv2.waitKey(10) & 0xFF == ord(constants.KILL_PROCESS_KEY_INPUT):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()