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
        
        lus = QLabel("Benutzername *")
        us = QLineEdit()
        lem = QLabel("E-Mail-Adresse *")
        em = QLineEdit()
        lps = QLabel("Passwort *")
        ps = QLineEdit()
        lpss = QLabel("Passwort wiederholen *")
        pss = QLineEdit()
        
        ly.addWidget(lvn, 0, 0)
        ly.addWidget(vn, 1, 0)
        ly.addWidget(lem, 2, 0)
        ly.addWidget(em, 3, 0)
        ly.addWidget(lag, 4, 0)
        ly.addWidget(ag, 5, 0)
        ly.addWidget(lgb, 6, 0)
        ly.addWidget(gb, 7, 0)
        
        ly.addWidget(lus, 0, 2)
        ly.addWidget(us, 1, 2)
        ly.addWidget(lnn, 2, 2)
        ly.addWidget(nn, 3, 2)
        ly.addWidget(lps, 4, 2)
        ly.addWidget(ps, 5, 2)
        ly.addWidget(lpss, 6, 2)
        ly.addWidget(pss, 7, 2)
        
        self.setLayout(ly)
        
        self.show()
        
        
app = QApplication(sys.argv) 
reg = registrer()
reg.show()
sys.exit(app.exec_())
