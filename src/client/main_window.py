from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSplashScreen, QSizePolicy 
from PyQt5.QtGui import QColor, QImage, QPixmap, QFont, QIcon
import sys
import cv2
import mediapipe as mp
import numpy as np
import constants.configuration
import core.process
import modules.voice_translate
import modules.detection
import modules.extract



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Define the colors
        background_color = QColor("#0D0D0D")  # Dark background color
        text_color = QColor("#FFFFFF")  # White text color
        button_color = QColor("#1E1E1E")  # Button background color
        button_hover_color = QColor("#333333")  # Button hover background color
        button_border_color = QColor("#707070")  # Button border color

        # Set the background color of the main window
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), background_color)
        self.setPalette(p)

        # Create main layout (horizontal)
        main_layout = QHBoxLayout(self)

        # Create layout for left section (camera)
        left_layout = QVBoxLayout()
        left_layout.setSpacing(0)  # Set spacing to 0 to eliminate margin

        # Add camera widget
        self.camera_widget = QLabel(self)
        self.camera_widget.setStyleSheet("border: 2px solid white; background-color: black;")
        self.camera_widget.setAlignment(Qt.AlignCenter)
        self.camera_widget.setMinimumSize(400, 400)  # Set minimum size for camera widget

        # Add camera widget to the left layout
        left_layout.addWidget(self.camera_widget)

        # Add left layout to the main layout
        main_layout.addLayout(left_layout)

        self.text_section_widget = QLabel("", self)
        self.text_section_widget.setStyleSheet("color: white; border: 2px solid white;")
        self.text_section_widget.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Align text to top-left
        self.text_section_widget.setWordWrap(True)  # Enable word wrapping
        self.text_section_widget.setFixedWidth(400)  # Set a fixed width for the text section
        self.text_section_widget.setFixedHeight(700)

        # Create quit button
        quit_button = QPushButton("Quit", self)
        quit_button.setStyleSheet("QPushButton { background-color: %s; color: %s; border: 2px solid %s; border-radius: 5px; }"
                                "QPushButton:hover { background-color: %s; }"
                                "QPushButton:pressed { background-color: %s; border: 2px solid %s; }" % (
                                    button_color.name(), text_color.name(), button_border_color.name(),
                                    button_hover_color.name(), button_hover_color.name(), text_color.name()))
        quit_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Set size policy for the button
        quit_button.setFixedWidth(400)  # Set a fixed width for the button
        quit_button.setFixedHeight(50)
        quit_button.clicked.connect(self.close)

        # Create a layout for the right side (text section and quit button)
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.text_section_widget)
        right_layout.addWidget(quit_button, alignment=Qt.AlignTop)  # Align button to top

        # Add the right layout to the main layout
        main_layout.addLayout(right_layout)

        # Set the stretch factor for the layouts
        main_layout.setStretch(0, 2)  # Left section occupies 2/3 of the main layout
        main_layout.setStretch(1, 1)  # Right section occupies 1/3 of the main layout

        # Set the main layout for the window
        self.setLayout(main_layout)

        # Set window title
        self.setWindowTitle("MHIA Application")

        # Set window size
        self.setMinimumSize(1440, 800)

        # Initialize Mediapipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=2)

        # Start the camera
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30 milliseconds

        # Initialize variables for main function
        self.sequence = []
        self.predictions = []
        self.latest_predicted_word = None
        self.threshold = 0.95
        self.model = core.process.load()
        self.word_seq = []

        self.mp_holistic = mp.solutions.holistic

        self.holistic = self.mp_holistic.Holistic(min_detection_confidence=constants.configuration.MIN_DETECTION_CONFIDENCE,
                                        min_tracking_confidence=constants.configuration.MIN_TRACKING_CONFIDENCE)

        # Load model (Replace 'process.load()' with the appropriate method to load your model)

    def update_frame(self):
        if not self.cap.isOpened():
            return

        # Check if a new frame is available
        ret, frame = self.cap.read()
        if not ret:
            return

        # Process every nth frame or skip frames if necessary
        if self.timer.isActive() and self.timer.remainingTime() > 0:
            return

        # Move image processing and prediction tasks to a separate thread
        # Consider using QThread for this purpose

        # Simplify the image processing pipeline or use a lighter-weight model if possible
        # This can include reducing the resolution of the input images or limiting the number of keypoints detected

        # Perform image processing with Mediapipe Hands
        img, results = modules.detection.mediapipe_detection(frame, self.holistic)

        keypoints = modules.extract.extract_key_values(results)

        self.sequence.append(keypoints)
        self.sequence = self.sequence[-30:]

        if len(self.sequence) == 30:
            if self.model is not None:
                res = self.model.predict(np.expand_dims(self.sequence, axis=0))[0]
                self.predictions.append(np.argmax(res))
                print(res[np.argmax(res)])
                if (len(self.predictions) >= 10 and 
                    np.unique(self.predictions[-10:])[0] == np.argmax(res) and 
                    res[np.argmax(res)] > self.threshold and 
                    self.latest_predicted_word != np.array(constants.configuration.ACTION_LIST)[np.argmax(res)]):

                    self.latest_predicted_word = np.array(constants.configuration.ACTION_LIST)[np.argmax(res)]
                    self.display_new_text(self.latest_predicted_word)

                    modules.voice_translate.voice_output(self.latest_predicted_word + "")
                    # You may perform further operations with the latest_predicted_word here

        # Convert processed frame to QImage
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img_rgb.shape
        bytes_per_line = 3 * width
        q_img = QImage(img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Scale image to fit the camera widget
        pixmap = QPixmap.fromImage(q_img)
        pixmap = pixmap.scaled(self.camera_widget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set pixmap to QLabel
        self.camera_widget.setPixmap(pixmap)

        # Restart the timer for the next frame processing
        self.timer.start(0)  # Update every 30 milliseconds



    def display_new_text(self, new_text):
        """
        Display the new text as a chat.
        """
        current_text = self.text_section_widget.text()
        if current_text:
            updated_text = current_text + " " + new_text
        else:
            updated_text = new_text
        self.text_section_widget.setText(updated_text)
