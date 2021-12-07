from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from page.page import Page


class Hello(Page):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('Hello World')
        self.label.move(100, 100)
        self.label.setStyleSheet("QLabel {font-size: 36px;}")
