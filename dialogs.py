from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("This is a dialog.")
        layout.addWidget(label, 0, 0)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttonbox)
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())