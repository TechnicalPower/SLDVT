import cv2

def mediapipe_detection(img, model):
    """
    Perform object detection using MediaPipe framework.

    Parameters:
        img: numpy.ndarray
            Input image in BGR color space.
        model: MediaPipe model
            Pre-trained MediaPipe model for object detection.

    Returns:
        tuple
            A tuple containing the processed image in BGR color space and the detection results.
    """
    if img is None or model is None:
        raise ValueError("Input image or model is None.")

    # Convert image color space to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process image with model
    results = model.process(img_rgb)

    # Convert image color space back to BGR
    img_processed = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

    return img_processed, results