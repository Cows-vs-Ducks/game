from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
import sys

class Svg(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ly = QGridLayout()

        pic = QSvgWidget("cow.svg")
        pic.setFixedSize(175, 200)
        ly.addWidget(pic, 0, 0)

        pic2 = QSvgWidget("cow.svg")
        pic2.setFixedSize(175, 200)
        ly.addWidget(pic2, 0, 1)
        
        self.setLayout(ly)

        self.show()

app = QApplication(sys.argv)
svg = Svg()
#svg.setGeometry(app.desktop())
svg.setWindowTitle("Cows vs. Ducks")
svg.show()
sys.exit(app.exec_())
