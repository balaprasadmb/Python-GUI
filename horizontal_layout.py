import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QWidget

app = QApplication([])

# Create label and button
label = QLabel('Hello, world!')
button = QPushButton('test')

layout = QHBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
widget = QWidget()
widget.setLayout(layout)
widget.show()

sys.exit(app.exec_())