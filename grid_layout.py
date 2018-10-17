import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget

app = QApplication([])


# Create label and button
label1 = QLabel('Label 1')
label2 = QLabel('Label 2')
label3 = QLabel('Label 3')
button = QPushButton('Press me!')
# Create layout and add widgets
layout = QGridLayout()
layout.addWidget(label1, 0, 0)
layout.addWidget(label2, 1, 0)
layout.addWidget(label3, 0, 1)
layout.addWidget(button, 1, 1)

widget = QWidget()
widget.setLayout(layout)
widget.show()

sys.exit(app.exec_())
