import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top= 150
        self.left= 150
        self.width = 500
        self.height = 500
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
#         painter.setPen(QPen(Qt.green, 8, Qt.DashLine))
#         painter.setPen(QPen(Qt.green, 8, Qt.DotLine))
#         painter.setPen(QPen(Qt.green, 8, Qt.DashDotLine))
#         painter.setPen(QPen(Qt.green, 8, Qt.DashDotDotLine))
#         painter.setPen(QPen(Qt.green, 8, Qt.CustomDashLine))
        painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
#         painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.Dense1Pattern))
#         painter.setBrush(QBrush(Qt.red, Qt.Dense2Pattern))
#         painter.setBrush(QBrush(Qt.red, Qt.Dense3Pattern))
#         painter.setBrush(QBrush(Qt.red, Qt.Dense4Pattern))
#         painter.setBrush(QBrush(Qt.red, Qt.Dense5Pattern))
#         painter.setBrush(QBrush(Qt.red, Qt.Dense6Pattern))
#         painter.setBrush(QBrush(Qt.red, Qt.Dense7Pattern))
#         painter.setBrush(QBrush(Qt.red, Qt.HorPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.VerPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.BDiagPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.FDiagPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.LinearGradientPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.RadialGradientPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.ConicalGradientPattern))
#         painter.setBrush(QBrush(Qt.red, Qt.TexturePattern))
        #draw circle
        painter.setBrush(QBrush(Qt.red, Qt.CrossPattern))
#         painter.drawEllipse(40, 40, 400, 400)
        #draw arc
        painter.begin(self)
        painter.setRenderHint(painter.Antialiasing)
#         painter.drawArc(100, 70, 300, 300, 0 * 16, 180 * 16)
        #draw a line
        painter.drawLine(0, 0, 200, 200)
        #draw a arrow
        painter.drawLine(400, 100, 100, 100)
        painter.drawLine(150, 150, 100, 100)
        painter.drawLine(150, 50, 100, 100)
    
app = QApplication(sys.argv)
 
window = Window()
 
sys.exit(app.exec())
