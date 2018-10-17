from PyQt5.QtWidgets import QApplication, QLabel
import sys

app = QApplication([])

label = QLabel('Hello, world!')
label.show()

sys.exit(app.exec_())
