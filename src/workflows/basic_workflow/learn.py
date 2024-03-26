import cv2
import mediapipe as mp
import numpy as np
import os
import constants
import core.process

class Learn:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.holistic = mp.solutions.holistic.Holistic(min_detection_confidence=constants.MIN_DETECTION_CONFIDENCE,
                                                        min_tracking_confidence=constants.MIN_TRACKING_CONFIDENCE)

    def start_capture(self):
        while True:
            if self.cap.isOpened():
                break

        for action in np.array(constants.ACTION_LIST):
            for sequence in range(constants.NP_SEQUENCE):
                for frame_num in range(constants.NP_LENGTH):
                    ret, frame = self.cap.read()
                    img, results = self.mediapipe_detection(frame)

                    self.draw_landmarks(img, results)
                    if frame_num == 0:
                        cv2.putText(img, 'STARTING COLLECTION', (120, 200),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                        cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(action, sequence),
                                    (15, 12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        cv2.imshow(constants.NAME_FRAME, img)
                        cv2.waitKey(2000)
                    else:
                        cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(action, sequence),
                                    (15, 12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        cv2.imshow(constants.NAME_FRAME, img)

                    keypoints = self.extract_key_values(results)
                    npy_path = os.path.join(os.path.join(constants.DATA_PATH_STRING), action, str(sequence),
                                            str(frame_num))
                    np.save(npy_path, keypoints)

                    if cv2.waitKey(10) & 0xFF == ord(constants.KILL_PROCESS_KEY_INPUT):
                        break

        self.process_data()
        self.cap.release()
        cv2.destroyAllWindows()