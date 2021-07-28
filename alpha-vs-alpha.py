from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
import sys

class Svg(QWidget):
    def __init__(self, app, parent=None):
        super().__init__(parent, app)

        ly = QGridLayout()

        size = app.desktop()
        
        self.stepw = size.width() / 20
        self.steph = size.height() / 15
        
        pic = QSvgWidget("cow.svg")
        pic.setFixedSize(175, 200)
        pic.move(size.width(), size.height()/2)
        pic.show()
        
        pic2 = QSvgWidget("cow.svg")
        pic2.setFixedSize(175, 200)
        pic2.move(0, size.height()/2)
        pic2.show()
        
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

app = QApplication(sys.argv)
svg = Svg(app)
#svg.setGeometry(app.desktop())
svg.setWindowTitle("Cows vs. Ducks")
svg.show()
sys.exit(app.exec_())
