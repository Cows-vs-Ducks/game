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
        
        l1.addWidget(lvn)
        w1.addWidget(vn)
        l2.addWidget(lnn)
        w2.addWidget(nn)
        l3.addWidget(lag)
        w3.addWidget(ag)
        l4.addWidget(lgb)
        w4.addWidget(gb)
        
        self.setLayout(l1)
        self.setLayout(w1)
        self.setLayout(l2)
        self.setLayout(w2)
        self.setLayout(l3)
        self.setLayout(w3)
        self.setLayout(l4)
        self.setLayout(w4)
        
        self.show()
        
        
app = QApplication(sys.argv) 
reg = rregistrer()
reg.show()
sys.exit(app.exec_())
