import numpy as np
import constants.configuration

"""
IMPORTANT!!
extract the data points of the movement
1. will be used on dataset collecting
2. will be used for evaluation session for sign language
"""


def extract_key_values(results):
    pose = (
        np.array(
            [
                [res.x, res.y, res.z, res.visibility]
                for res in results.pose_landmarks.landmark
            ]
        ).flatten()
        if results.pose_landmarks
        else np.zeros(constants.configuration.SIZE_POSE_LANDMARK)
    )
    face = (
        np.array(
            [[res.x, res.y, res.z] for res in results.face_landmarks.landmark]
        ).flatten()
        if results.face_landmarks
        else np.zeros(constants.configuration.SIZE_FACE_LANDMARK)
    )
    left_hand = (
        np.array(
            [[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]
        ).flatten()
        if results.left_hand_landmarks
        else np.zeros(constants.configuration.SIZE_LEFT_HAND_LANDMARK)
    )
    right_hand = (
        np.array(
            [[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]
        ).flatten()
        if results.right_hand_landmarks
        else np.zeros(constants.configuration.SIZE_RIGHT_HAND_LANDMARK)
    )
    return np.concatenate([pose, face, left_hand, right_hand])
