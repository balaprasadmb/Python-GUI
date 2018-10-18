from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        hscrollbar = QScrollBar()
        hscrollbar.setOrientation(Qt.Horizontal)
        vscrollbar = QScrollBar()
        vscrollbar.setOrientation(Qt.Vertical)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())