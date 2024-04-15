from PyQt5.QtCore import Qt, QTimer
from client import main_window
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSplashScreen
from PyQt5.QtGui import QPixmap
import sys

class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

def main():
    # Example usage:
    app = QApplication(sys.argv)

    # Load splash screen image
    splash_img = QPixmap("../figure/splash.png")
    splash = SplashScreen(splash_img)
    splash.show()

    # Do any necessary initialization here...

    # Close the splash screen after some time (e.g., 3 seconds)
    QTimer.singleShot(3000, splash.close)

    # Create and show the main window
    window = main_window.MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
