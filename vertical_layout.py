import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

app = QApplication([])

# Create label and button
label = QLabel('Hello, world!')
button = QPushButton('test')

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
widget = QWidget()
widget.setLayout(layout)
widget.show()

sys.exit(app.exec_())