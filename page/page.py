from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Page(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Welcome Application'
        self.width = 640
        self.height = 480
        self.icon = 'resource/icon.png'

        self.setWindowTitle(self.title)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon(self.icon))

    def changePage(self, page):
        self.close()
        self.page = page
        self.page.show()
