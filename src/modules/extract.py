import numpy as np
import constants.configuration as configuration
"""
IMPORTANT!!
extract the data points of the movement
1. will be used on dataset collecting
2. will be used for evaluation session for sign language
"""
def extract_key_values(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(configuration.SIZE_POSE_LANDMARK)
    left_hand = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(configuration.SIZE_LEFT_HAND_LANDMARK)
    right_hand = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(configuration.SIZE_RIGHT_HAND_LANDMARK)
    
    face_oval = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[configuration.FACE_OVAL]]).flatten() if results.face_landmarks else np.zeros(len(configuration.FACE_OVAL) * 3)
    lips = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[configuration.FACE_LIPS]]).flatten() if results.face_landmarks else np.zeros(len(configuration.FACE_LIPS) * 3)
    right_eye = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[configuration.RIGHT_EYE]]).flatten() if results.face_landmarks else np.zeros(len(configuration.RIGHT_EYE) * 3)
    left_eye = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[configuration.LEFT_EYE]]).flatten() if results.face_landmarks else np.zeros(len(configuration.LEFT_EYE) * 3)
    right_eyebrow = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[configuration.RIGHT_EYEBROW]]).flatten() if results.face_landmarks else np.zeros(configuration.EYEBROW_LANDMARK * 3)
    left_eyebrow = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[configuration.LEFT_EYEBROW]]).flatten() if results.face_landmarks else np.zeros(configuration.EYEBROW_LANDMARK * 3)


    return np.concatenate([pose, face_oval, lips, right_eye, left_eye, right_eyebrow, left_eyebrow, left_hand, right_hand])




    # face_oval = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[mp_face_mesh.FACEMESH_FACE_OVAL]]).flatten() if results.face_landmarks else np.zeros(len(mp_face_mesh.FACEMESH_FACE_OVAL) * 3)
    # lips = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[mp_face_mesh.FACEMESH_LIPS]]).flatten() if results.face_landmarks else np.zeros(len(mp_face_mesh.FACEMESH_LIPS) * 3)
    # left_eye = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[mp_face_mesh.FACEMESH_LEFT_EYE]]).flatten() if results.face_landmarks else np.zeros(len(mp_face_mesh.FACEMESH_LEFT_EYE) * 3)
    # right_eye = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark[mp_face_mesh.FACEMESH_RIGHT_EYE]]).flatten() if results.face_landmarks else np.zeros(len(mp_face_mesh.FACEMESH_RIGHT_EYE) * 3)
    
    # left_hand = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(constants.configuration.SIZE_LEFT_HAND_LANDMARK)
    # right_hand = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(constants.configuration.SIZE_RIGHT_HAND_LANDMARK)
    
    # return np.concatenate([pose, face_oval, lips, left_eye, right_eye, left_hand, right_hand])