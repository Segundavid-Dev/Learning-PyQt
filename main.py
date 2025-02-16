import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QSize
from random import choice


window_titles = [
    "Good App",
    "Great App",
    "Best App",
    "Wonderful App"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Awesome App")

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
    
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")
    
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
    # signals and slots
    # events




# instanciation
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()