import cv2
import mediapipe as mp
import numpy as np
import os
import constants.configuration
import modules.detection
import modules.extract
import modules.draw
import core.process
import utils.data_generate as data_generate

class Learn:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.holistic = mp.solutions.holistic.Holistic(min_detection_confidence=constants.configuration.MIN_DETECTION_CONFIDENCE,
                                                        min_tracking_confidence=constants.configuration.MIN_TRACKING_CONFIDENCE)

    def start_capture(self, word):
        while True:
            if self.cap.isOpened():
                break

        for sequence in range(constants.configuration.NP_SEQUENCE):
            for frame_num in range(constants.configuration.NP_LENGTH):
                ret, frame = self.cap.read()
                img, results = modules.detection.mediapipe_detection(frame, self.holistic)

                modules.draw.draw_landmarks(img, results)
                if frame_num == 0:
                    cv2.putText(img, 'STARTING COLLECTION', (120, 200),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                    cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(word, sequence),
                                (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.imshow(constants.configuration.NAME_FRAME, img)
                    cv2.waitKey(2000)
                else:
                    cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(word, sequence),
                                (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.imshow(constants.configuration.NAME_FRAME, img)

                keypoints = modules.extract.extract_key_values(results)
                npy_path = os.path.join(os.path.join(constants.configuration.DATA_PATH_CUSTOM), word, str(sequence), str(frame_num))
                np.save(npy_path, keypoints)

                if cv2.waitKey(10) & 0xFF == ord(constants.configuration.KILL_PROCESS_KEY_INPUT):
                    break

        print("PROCESS SHOULD BE PERFORMED TO MAKE DATASET WEIGHT ON THE MODEL!!: Required prompt : python3 process.py process_custom_flow")

        self.cap.release()
        cv2.destroyAllWindows()


def main():
    data_generate.custom_flow_data_generate("HELLO")
    # basic_learn = Learn()
    # basic_learn.start_capture()


if __name__ == "__main__":
    main()
