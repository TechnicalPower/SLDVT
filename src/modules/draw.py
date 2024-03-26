import mediapipe

#holistic model for image detection taking landmarks
mp_holistic = mediapipe.solutions.holistic

#image drawing on the frame model
mp_drawing = mediapipe.solutions.drawing_utils

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