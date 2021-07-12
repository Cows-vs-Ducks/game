from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class registrer(QWidget): 
    def __init__(self, parent=None): 
        super().__init__(parent)
        
        ly = QGridLayout()
        
        lvn = QLabel("Vorname")
        vn = QLineEdit()
        lnn = QLabel("Nachname")
        nn = QLineEdit()
        lag = QLabel("Alter")
        ag = QLineEdit()
        lgb = QLabel("Geburtsdatum (tt, mm, jjjj)")
        gb = QLineEdit()
        
        ly.addWidget(lvn)
        ly.addWidget(vn)
        ly.addWidget(lnn)
        ly.addWidget(nn)
        ly.addWidget(lag)
        ly.addWidget(ag)
        ly.addWidget(lgb)
        ly.addWidget(gb)
        
        self.setLayout(ly)
        
        self.show()
        
        
app = QApplication(sys.argv) 
reg = registrer()
reg.show()
sys.exit(app.exec_())
