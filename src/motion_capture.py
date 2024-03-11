import cv2
import numpy as np
import os 
from matplotlib import pyplot
from keras.models import Sequential

import time
import mediapipe
import constants
import process
import voice_translate
#holistic model for image detection taking landmarks
mp_holistic = mediapipe.solutions.holistic

#image drawing on the frame model
mp_drawing = mediapipe.solutions.drawing_utils


## REFERENCED FROM YOUTUBE https://www.youtube.com/watch?v=doDUihpj6ro
# colors = [(245,117,16), (117,245,16), (16,117,245)]


# def prob_viz(res, actions, input_frame, colors):
#     output_frame = input_frame.copy()
#     for num, prob in enumerate(res):
#         cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors[num], -1)
#         cv2.putText(output_frame, actions[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
#     return output_frame

def mediapipe_detection(img, model):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img.flags.writeable = False
    results = model.process(img)
    img.flags.writeable = True
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img, results


"""
draw the landmark over the img on the fram
1. face_landmarks
2. pose_landmarks
3. left_hand_landmarks
4. right_hand_landmarks

Possibly will be removed once UX/UI is deployed
"""
def draw_landmarks(img, results):
    mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
    mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)


"""
IMPORTANT!!
extract the data points of the movement
1. will be used on dataset collecting
2. will be used for evaluation session for sign language
"""
def extract_key_values(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(constants.SIZE_POSE_LANDMARK)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(constants.SIZE_FACE_LANDMARK)
    left_hand = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(constants.SIZE_LEFT_HAND_LANDMARK)
    right_hand = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(constants.SIZE_RIGHT_HAND_LANDMARK)
    return np.concatenate([pose, face, left_hand, right_hand])

"""
class main_for_learning is for learning flow:
* User is not able to be in this flow (only for admin and testing, dataset collecting purpose)
"""
def main_for_learning():
    
    # VideoCapture with input 0 will call the camera to get motion captured
    # Reference: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#ae82ac8efcff2c5c96be47c060754a518
    cap = cv2.VideoCapture(0)
    # Returns true if video capturing has been initialized already
    with mp_holistic.Holistic(min_detection_confidence=constants.MIN_DETECTION_CONFIDENCE,
                               min_tracking_confidence=constants.MIN_TRACKING_CONFIDENCE) as holistic:
        while True:
            if cap.isOpened():
                break
        for action in np.array(constants.ACTION_LIST):
            # Grabs, decodes and returns the next video frame
            for sequence in range(constants.NP_SEQUENCE):
                
                for frame_num in range(constants.NP_LENGTH):
                            
                    # ret :
                    # frame : 
                    ret, frame = cap.read()
                    img, results = mediapipe_detection(frame,holistic)

                    draw_landmarks(img, results)
                    if frame_num == 0:
                        cv2.putText(img, 'STARTING COLLECTION', (120, 200),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                        cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15, 12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0,255), 1, cv2.LINE_AA)
                        cv2.imshow(constants.NAME_FRAME, img)
                        cv2.waitKey(2000)
                    else:
                        cv2.putText(img, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15, 12),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 1, cv2.LINE_AA)
                        cv2.imshow(constants.NAME_FRAME, img)
                    
                    keypoints = extract_key_values(results)
                    npy_path = os.path.join(os.path.join(constants.DATA_PATH_STRING), action, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)

                    if cv2.waitKey(10) & 0xFF == ord(constants.KILL_PROCESS_KEY_INPUT):
                        break
        process.process()

        cap.release()
        cv2.destroyAllWindows()
def main_beta():
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


def main():
    sequence = []
    predictions = []
    latest_predicted_word = None  # Initialize variable to store the latest predicted word
    threshold = 0.95

    cap = cv2.VideoCapture(0)
    model = process.load()

    with mp_holistic.Holistic(min_detection_confidence=constants.MIN_DETECTION_CONFIDENCE,
                               min_tracking_confidence=constants.MIN_TRACKING_CONFIDENCE) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            img, results = mediapipe_detection(frame, holistic)

            keypoints = extract_key_values(results)

            sequence.append(keypoints)
            sequence = sequence[-30:]
            print(len(sequence))
            print(len(predictions))

            if len(sequence) == 30:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                predictions.append(np.argmax(res))
                print(np.array(constants.ACTION_LIST)[np.argmax(res)])
                if len(predictions) >= 10 and np.unique(predictions[-10:])[0] == np.argmax(res) and res[np.argmax(res)] > threshold and latest_predicted_word != np.array(constants.ACTION_LIST)[np.argmax(res)]:
                    latest_predicted_word = np.array(constants.ACTION_LIST)[np.argmax(res)]
                    voice_translate.voice_output(latest_predicted_word + "")
                    print("THRESHOLD" + latest_predicted_word)
                    # You may perform further operations with the latest_predicted_word here
            cv2.imshow(constants.NAME_FRAME, img)

            if cv2.waitKey(10) & 0xFF == ord(constants.KILL_PROCESS_KEY_INPUT):
                break

    cap.release()
    cv2.destroyAllWindows()  

if __name__ == "__main__":
    var_workflow = input("Hello! Welcome to Sign Language Detection Service. You are currently in admin-only available service. If you want to make new dataset, press 'L'. Otherwise, press any key")
    if(var_workflow == constants.FLOW_LEARNING):
        print("Learning mode activated")
        main_for_learning()
    else:
        print("User level mode activated")
        main()

