from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from page.hello import Hello

from page.page import Page


class Welcome(Page):
    def __init__(self):
        super().__init__()

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

        self.button = QPushButton('Start', self)
        self.button.move(50, 300)
        self.button.setStyleSheet(
            """QPushButton {font-size: 18px; font-weight: bold; color: #04045C; font-family: Arial; background-color: #F5F5F5; border-radius: 10px; border: 2px solid #04045C; padding: 8px 24px; }
            QPushButton:hover {background-color: #04045C; color: #F5F5F5; }
            QPushButton:pressed {background-color: #020202; color: #F5F5F5; }""")
        self.button.clicked.connect(self.on_click)

        self.notes = QLabel(self)
        self.notes.setText(
            'Notes: You can delete this page and create your own page or edit hello.py file.')
        # move the notes to the bottom of the window
        self.notes.move(50, self.height - 50)
        self.notes.setStyleSheet(
            "QLabel {font-size: 12px; color: #04045C; font-family: Arial; }")

    def on_click(self):
        self.switchPage(Hello())
