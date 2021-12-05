from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QMainWindow
import sys


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Login'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()
        self.show()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('Enter your name:')
        self.label.move(20, 20)

        self.line = QLineEdit(self)
        self.line.move(20, 40)
        self.line.resize(280, 40)

        self.button = QPushButton('Submit', self)
        self.button.move(20, 80)

        self.button2 = QPushButton('Quit', self)
        self.button2.move(20, 120)
        self.button2.clicked.connect(sys.exit)
