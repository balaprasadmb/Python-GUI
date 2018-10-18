from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        calendar = QCalendarWidget()
        layout.addWidget(calendar)
        datetimeedit = QDateTimeEdit()
        datetimeedit.dateTime()
        datetimeedit.setCalendarWidget(calendar)
        layout.addWidget(datetimeedit)
        

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())