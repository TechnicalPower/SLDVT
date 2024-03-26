import cv2
import numpy as np
import mediapipe as mp
import constants
import utils.data_generate
import os
import utils.action_parser
import modules.draw

class CustomFlowLearn:
    def __init__(self):
        self.mp_holistic = mp.solutions.holistic

    def learn_custom_flow(self):
        word = input("Currently in custom flow... Could you tell me which word you want to teach for me?")
        utils.data_generate.custom_flow_data_generate(word)

        cap = cv2.VideoCapture(0)
        with self.mp_holistic.Holistic(min_detection_confidence=constants.MIN_DETECTION_CONFIDENCE,
                                   min_tracking_confidence=constants.MIN_TRACKING_CONFIDENCE) as holistic:
            while True:
                if cap.isOpened():
                    break

            for sequence in range(constants.NP_SEQUENCE):
                for frame_num in range(constants.NP_LENGTH):
                    ret, frame = cap.read()
                    img, results = self.mediapipe_detection(frame, holistic)

                    modules.draw.draw_landmarks(img, results)
                    if frame_num == 0:
                        cv2.putText(img, 'STARTING COLLECTION', (120, 200),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                        cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(word, sequence),
                                    (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        cv2.imshow(constants.NAME_FRAME, img)
                        cv2.waitKey(2000)
                    else:
                        cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(word, sequence),
                                    (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        cv2.imshow(constants.NAME_FRAME, img)

                    keypoints = self.extract_key_values(results)
                    npy_path = os.path.join(os.path.join(constants.DATA_PATH_CUSTOM), word, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)

                    if cv2.waitKey(10) & 0xFF == ord(constants.KILL_PROCESS_KEY_INPUT):
                        break

        print("PROCESS SHOULD BE PERFORMED TO MAKE DATASET WEIGHT ON THE MODEL!!: Required prompt : python3 process.py process_custom_flow")
        utils.action_parser.append_action("actions.txt", word)

        cap.release()
        cv2.destroyAllWindows()

def main():
    custom_flow_learner = CustomFlowLearn()
    custom_flow_learner.learn_custom_flow()

if __name__ == "__main__":
    main()
