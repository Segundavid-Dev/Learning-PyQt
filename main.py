import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QSlider,
    QTimeEdit,
    QPushButton,
    QSpinBox,
    QRadioButton,
    QDoubleSpinBox,
)
from PyQt5.QtGui import QPixmap
# working with layouts
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        self.setGeometry(0,0,400,400)

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        self.setCentralWidget(widget)



# instanciation
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()