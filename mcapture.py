import cv2
import numpy
import os 
from matplotlib import pyplot
import time
import mediapipe

def main():
    # VideoCapture with input 0 will call the camera to get motion captured
    # Reference: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#ae82ac8efcff2c5c96be47c060754a518
    cap = cv2.VideoCapture(0)

    # Returns true if video capturing has been initialized already
    while cap.isOpened():
        # Grabs, decodes and returns the next video frame
        # ret :
        # frame : 
        ret, frame = cap.read()
        cv2.imshow('Motion Capture', frame)

        #break for frame closure
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()