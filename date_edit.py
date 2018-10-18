from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        date_widget = QDate()
        date_widget.setDate(18, 12, 1996)
        date_edit = QDateEdit()
        date_edit.setDate(date_widget)
        layout.addWidget(date_edit, 0, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())