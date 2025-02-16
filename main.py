import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt, QSize
from random import choice


window_titles = [
    'My App',
    'Still My App',
    'What on earth',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python GUI")

        # widgets
        self.button = QPushButton("press me")
        self.setCentralWidget(self.button)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked) # signal -> button clicked
        self.windowTitleChanged.connect(self.the_window_title_changed) # signal -> windowTitleChanged

    # storing the state of widgets in variable
    # changing the interface
    def the_button_was_clicked(self):
        print("clicked!")
        new_window_title = choice(window_titles)
        print(f"Setting title {new_window_title}")
        self.setWindowTitle(new_window_title)
    
    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}")
        if window_title == 'Something went wrong':
            self.button.setEnabled(False)


# instanciation
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()














# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
# from PyQt5.QtGui import *
# from PyQt5.QtCore import QSize, Qt



# class MainWindow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__()





# # instanciation
# app = QApplication(sys.argv)

# window = MainWindow() 
# window.show() #IMPORTANT

# sys.argv(app.exec_())