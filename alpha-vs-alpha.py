from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
import sys, os

class Svg(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ly = QGridLayout()

        fileh = open("height.cvd", "r")
        self.height = fileh.read()
        fileh.close()
        filew = open("width.cvd", "r")
        self.width = filew.read()
        filew.close()
        
        self.stepw = int(self.width) / 20
        self.steph = int(self.height()) / 15
        
        pic = QSvgWidget("cow.svg")
        pic.setFixedSize(175, 200)
        pic.move(int(self.width()), int(self.height()) / 2)
        
        pic2 = QSvgWidget("cow.svg")
        pic2.setFixedSize(175, 200)
        pic2.move(0, int(self.height()) / 2)
        
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
        
    def right(self):
        pass
    
    def down(self):
        pass
    
    def left(self):
        pass
    
    def up(self):
        pass

app = QApplication([])
try:
    os.remove("width.cvd")
    os.remove("height.cvd")
except:
    pass
filew = open("width.cvd", "a")
filew.write(str(app.desktop().width()))
filew.close()
fileh = open("height.cvd", "a")
fileh.write(str(app.desktop().height()))
fileh.close()
svg = Svg()
#svg.setGeometry(app.desktop())
svg.setWindowTitle("Cows vs. Ducks")
svg.show()
sys.exit(app.exec_())
