from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.doublespinbox = QDoubleSpinBox()
        self.doublespinbox.setValue(9.0)
        self.doublespinbox.setMinimum(3.0)
        self.doublespinbox.setMaximum(19.0)
        self.doublespinbox.setRange(10.0, 30.0)
        self.doublespinbox.setPrefix('Rs. ')
        self.doublespinbox.setSuffix(' Rupees')
        self.doublespinbox.setSingleStep(1)
        self.doublespinbox.valueChanged.connect(self.spin_changed)
        layout.addWidget(self.doublespinbox)

    def spin_changed(self):
        print("Current Spin value: %i" % (self.doublespinbox.value()))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())