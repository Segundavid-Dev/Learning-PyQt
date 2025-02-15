import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()


        self.setWindowTitle("My Awesome App")
        label = QLabel("THIS IS AWESOME")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        


# instanciation
app = QApplication(sys.argv)

window = MainWindow() 
window.show() #IMPORTANT

sys.argv(app.exec_())