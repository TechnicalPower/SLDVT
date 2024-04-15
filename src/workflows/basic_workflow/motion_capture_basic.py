import cv2
import numpy as np
import mediapipe as mp
import constants
import core.process
import modules.voice_translate
import modules.detection
import modules.extract


class MotionCapture:
    def __init__(self):
        self.sequence = []
        self.predictions = []
        self.latest_predicted_word = None
        self.threshold = 0.95
        self.cap = cv2.VideoCapture(0)
        self.model = core.process.load()
        self.mp_holistic = mp.solutions.holistic

    def run(self):
        with self.mp_holistic.Holistic(min_detection_confidence=constants.MIN_DETECTION_CONFIDENCE,
                                        min_tracking_confidence=constants.MIN_TRACKING_CONFIDENCE) as holistic:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break
                
                img, results = modules.detection.mediapipe_detection(frame, holistic)

                keypoints = modules.extract.extract_key_values(results)

                self.sequence.append(keypoints)
                self.sequence = self.sequence[-30:]
                print(len(self.sequence))
                print(len(self.predictions))

                if len(self.sequence) == 30:
                    res = self.model.predict(np.expand_dims(self.sequence, axis=0))[0]
                    self.predictions.append(np.argmax(res))
                    print(np.array(constants.ACTION_LIST)[np.argmax(res)])
                    if len(self.predictions) >= 10 and np.unique(self.predictions[-10:])[0] == np.argmax(res) and res[np.argmax(res)] > self.threshold and self.latest_predicted_word != np.array(constants.ACTION_LIST)[np.argmax(res)]:
                        self.latest_predicted_word = np.array(constants.ACTION_LIST)[np.argmax(res)]
                        modules.voice_translate.voice_output(self.latest_predicted_word + "")
                        print("THRESHOLD" + self.latest_predicted_word)
                        # You may perform further operations with the latest_predicted_word here
                cv2.imshow(constants.NAME_FRAME, img)

                if cv2.waitKey(10) & 0xFF == ord(constants.KILL_PROCESS_KEY_INPUT):
                    break

        self.cap.release()
        cv2.destroyAllWindows()


def main():
    motion_capture = MotionCapture()
    motion_capture.run()


if __name__ == "__main__":
    main()
