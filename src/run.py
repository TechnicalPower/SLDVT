from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
import sys

from client.main_window import MainWindow
from client.splash_screen import SplashScreen

def main():
    # Initialize the PyQt application
    app = QApplication(sys.argv)

    # Load the splash screen image
    splash_img = QPixmap("figure/splash.png")

    # Create and show the splash screen
    splash = SplashScreen(splash_img)
    splash.show()

    # Do any necessary initialization here...

    # Close the splash screen after some time (e.g., 3 seconds)
    QTimer.singleShot(3000, splash.close)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Execute the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
