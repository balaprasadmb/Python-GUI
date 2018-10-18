from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.spinbox = QSpinBox()
        self.spinbox.setValue(9)
        self.spinbox.setMinimum(3)
        self.spinbox.setMaximum(19)
        self.spinbox.setRange(10, 30)
        self.spinbox.setPrefix('Rs. ')
        self.spinbox.setSuffix(' Rupees')
        self.spinbox.setSingleStep(1)
        self.spinbox.valueChanged.connect(self.spin_changed)
        layout.addWidget(self.spinbox)

    def spin_changed(self):
        print("Current Spin value: %i" % (self.spinbox.value()))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())