from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSizePolicy, QWidget, QApplication, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QMainWindow
import sys
from model.user import User

app = QApplication(sys.argv)


class PageTest(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Page Test'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: #FFFFFF;")
        self.setWindowIcon(QIcon("resource/icon.png"))

        self.initUI()
        self.show()

    def initUI(self):
        self.label = QLabel(self)

        user = User()
        user = user.find(1)

        self.label.setText(user["email"] + "\n" + str(user["created_at"]))
        self.label.move(70, 180)
        self.label.setStyleSheet("QLabel {font-size: 36px;}")

    def run(self):
        app.exec_()
