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
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # set central widget of the window
        self.setCentralWidget(container)
        
    # signals and slots




# instanciation
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()