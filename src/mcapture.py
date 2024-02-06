import cv2
import numpy
import os 
from matplotlib import pyplot
import time
import mediapipe

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
def main():
    # VideoCapture with input 0 will call the camera to get motion captured
    # Reference: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#ae82ac8efcff2c5c96be47c060754a518
    cap = cv2.VideoCapture(0)

    # Returns true if video capturing has been initialized already
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            # Grabs, decodes and returns the next video frame
            # ret :
            # frame : 
            ret, frame = cap.read()
            img, results = mediapipe_detection(frame,holistic)
            draw_landmarks(img, results)
            cv2.imshow('Motion Capture', img)
            print(results)
            #break for frame closure with typing 'q'
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()