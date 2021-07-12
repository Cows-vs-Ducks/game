from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class registrer(QWidget): 
    def __init__(self, parent=None): 
        super().__init__(parent)
        
        l1 = QHBoxLayout()
        w1 = QHBoxLayout()
        l2 = QHBoxLayout()
        w2 = QHBoxLayout()
        l3 = QHBoxLayout()
        w3 = QHBoxLayout()
        l4 = QHBoxLayout()
        w4 = QHBoxLayout()
        
        lvn = QLabel("Vorname")
        vn = QLineEdit()
        lnn = QLabel("Nachname")
        nn = QLineEdit()
        lag = QLabel("Alter")
        ag = QLineEdit()
        lgb = QLabel("Geburtsdatum (tt, mm, jjjj)")
        gb = QLineEdit()
        
        
        
app = QApplication(sys.argv) 
reg = registrer()
reg.resize(app.desktop()) 
reg.show()
sys.exit(app.exec_())
