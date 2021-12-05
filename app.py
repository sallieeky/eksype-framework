from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QMainWindow
import sys

from pages.welcome import Welcome


class App():
    def __init__(self):
        self.initWindow = Welcome()
        self.initWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
