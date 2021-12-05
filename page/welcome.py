from PyQt5.QtCore import *
from PyQt5.QtWidgets import QSizePolicy, QWidget, QApplication, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QMainWindow


class Welcome(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Welcome App'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('Welcome to Eksype Framework')
        self.label.move(70, 180)
        self.label.setStyleSheet("QLabel {font-size: 36px;}")
