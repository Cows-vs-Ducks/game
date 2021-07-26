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
        pic.move(0, 0)
        
        pic2 = QSvgWidget("cow.svg")
        pic2.setFixedSize(175, 200)
        pic2.move(0, 0)
        
        self.setLayout(ly)

        self.show()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.right()
        elif event.key() == Qt.Key_Down:
            self.down()
        elif event.key() == Qt.Key_Left:
            self.left()
        elif event.key() == Qt.Key_Up:
            self.up()
        else:
            pass
        
        event.accept()

app = QApplication(sys.argv)
svg = Svg()
#svg.setGeometry(app.desktop())
svg.setWindowTitle("Cows vs. Ducks")
svg.show()
sys.exit(app.exec_())
