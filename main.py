import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar
from PyQt5.QtGui import QPalette, QColor
# working with layouts
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("My Awesome App")
        label = QLabel("Hello")
        self.setCentralWidget(label)

        toolbar = QToolBar("my main toolbar")
        self.addToolBar(toolbar)
# instanciation
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()