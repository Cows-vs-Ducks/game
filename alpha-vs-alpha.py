from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
import sys, os

class Svg(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ly = QHBoxLayout()

        fileh1 = open("height.cvd", "r")
        self.height = fileh1.read()
        fileh1.close()
        filew1 = open("width.cvd", "r")
        self.width = filew1.read()
        filew1.close()
        
        self.stepw = int(self.width) / 20
        self.steph = int(self.height) / 15
        
        self.keyUp = "16777235"
        self.keyDown = "16777237"
        self.keyLeft = "16777234"
        self.keyRight = "16777236"
        
        self.cowx = 0
        self.cowy = int(self.height) / 2
        self.duckx = int(self.width) - 200
        self.ducky = int(self.height) / 2
        
        pic = QSvgWidget("cow.svg", self) # Cow
        pic.setFixedSize(175, 200)
        pic.move(self.cowx, self.cowy)
        
        pic2 = QSvgWidget("cow.svg", self) # Duck
        pic2.setFixedSize(175, 200)
        pic2.move(self.duckx, self.ducky)
        
        
        self.setLayout(ly)

        self.showFullScreen()
        
    def keyPressEvent(self, event):
        if str(event.key()) == self.keyRight:
            self.right()
        elif str(event.key()) == self.keyDown:
            self.down()
        elif str(event.key()) == self.keyLeft:
            self.left()
        elif str(event.key()) == self.keyUp:
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
svg.setWindowTitle("Cows vs. Ducks")
svg.show()
sys.exit(app.exec_())
