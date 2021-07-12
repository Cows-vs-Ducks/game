from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class registrer(QWidget): 
    def __init__(self, parent=None): 
        super().__init__(parent)
        
        nm = QLineEdit()
        
app = QApplication(sys.argv) 
reg = registrer()
reg.resize(app.desktop()) 
reg.show()
sys.exit(app.exec_())
