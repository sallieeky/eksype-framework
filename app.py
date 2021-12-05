from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QMainWindow
import sys
from helper.auth import Auth
from helper.db import DB

from pages.loginpage import Login


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'My App'
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
        self.label.setText('Enter your username:')
        self.label.move(20, 20)

        self.line = QLineEdit(self)
        self.line.move(20, 40)
        self.line.resize(280, 40)

        self.label2 = QLabel(self)
        self.label2.setText('Enter your password:')
        self.label2.move(20, 80)

        self.line2 = QLineEdit(self)
        self.line2.move(20, 100)
        self.line2.resize(280, 40)

        self.button = QPushButton('Login', self)
        self.button.move(20, 160)
        self.button.clicked.connect(self.changePage)

    def changePage(self):
        username = self.line.text()
        password = self.line2.text()

        auth = Auth().login(username, password)
        if(auth):
            self.hide()
            self.login = Login()
            self.login.show()

        else:
            QMessageBox.about(self, 'Error', 'Invalid username or password')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
