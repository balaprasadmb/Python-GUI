import sys
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication([])

button = QPushButton('Say hello')

def say_hello(event):
    print('Hello World!')

button.clicked.connect(say_hello)

button.show()

sys.exit(app.exec_())