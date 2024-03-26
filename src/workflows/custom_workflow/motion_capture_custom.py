import cv2
import numpy as np
import mediapipe as mp
import constants
import core.process
import utils.action_parser
import modules.voice_translate

class CustomFlowMain:
    def __init__(self):
        self.mp_holistic = mp.solutions.holistic

    def run_custom_flow(self):
        sequence = []
        predictions = []
        latest_predicted_word = None  # Initialize variable to store the latest predicted word
        threshold = 0.95

        action_list = np.array(utils.action_parser.parse_actions("actions.txt"))

        cap = cv2.VideoCapture(0)
        model = core.process.load_custom_flow()

        with self.mp_holistic.Holistic(min_detection_confidence=constants.MIN_DETECTION_CONFIDENCE,
                                       min_tracking_confidence=constants.MIN_TRACKING_CONFIDENCE) as holistic:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                img, results = self.mediapipe_detection(frame, holistic)

                keypoints = self.extract_key_values(results)

                sequence.append(keypoints)
                sequence = sequence[-30:]
                print(len(sequence))
                print(len(predictions))

                if len(sequence) == 30:
                    res = model.predict(np.expand_dims(sequence, axis=0))[0]
                    predictions.append(np.argmax(res))
                    print(action_list[np.argmax(res)])
                    if len(predictions) >= 10 and np.unique(predictions[-10:])[0] == np.argmax(res) and res[np.argmax(res)] > threshold and latest_predicted_word != action_list[np.argmax(res)]:
                        latest_predicted_word = action_list[np.argmax(res)]
                        modules.voice_translate.voice_output(latest_predicted_word + "")
                        print("THRESHOLD" + latest_predicted_word)
                        # You may perform further operations with the latest_predicted_word here
                cv2.imshow(constants.NAME_FRAME, img)

                if cv2.waitKey(10) & 0xFF == ord(constants.KILL_PROCESS_KEY_INPUT):
                    break

        cap.release()
        cv2.destroyAllWindows()  

def custom_flow_main():
    custom_flow = CustomFlowMain()
    custom_flow.run_custom_flow()

if __name__ == "__main__":
    custom_flow_main()
