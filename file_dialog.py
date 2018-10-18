from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.ledit = QLineEdit()
        layout.addWidget(self.ledit, 0, 0)
        select_file = QPushButton("Select File")
        select_file.clicked.connect(self.on_select_file)
        layout.addWidget(select_file,0, 1)
        self.filedialog = QFileDialog()

    def on_select_file(self):
        self.filedialog.open()
        self.filedialog.setAcceptMode(QFileDialog.AcceptOpen)
        self.ledit.setText(self.filedialog.getOpenFileName()[0])

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())