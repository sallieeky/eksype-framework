from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
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
        self.setWindowIcon(QIcon('resource/icon.png'))
        self.setStyleSheet("QWidget {background-color: #ffffff;}")

        self.initUI()

    def initUI(self):
        self.icon = QLabel(self)
        self.icon.setPixmap(QIcon('resource/icon.png').pixmap(QSize(200, 200)))
        self.icon.move(50, 50)

        self.label = QLabel(self)
        self.label.setText('Welcome to Eksype Framework')
        self.label.move(50, 180)
        self.label.setStyleSheet(
            "QLabel {font-size: 36px; font-weight: bold; color: #04045C; font-family: Arial; }")

        self.copyright = QLabel(self)
        self.copyright.setText(
            'Copyright © 2021 Sallie Trixie Zebada Mansurina')
        self.copyright.move(50, 220)
        self.copyright.setStyleSheet(
            "QLabel {font-size: 12px; color: #04045C; font-family: Arial; }")
