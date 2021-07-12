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
        ly.addWidget(lnn, 2, 0)
        ly.addWidget(nn, 3, 0)
        ly.addWidget(lag, 4, 0)
        ly.addWidget(ag, 5, 0)
        ly.addWidget(lgb, 6, 0)
        ly.addWidget(gb, 7, 0)
        
        self.setLayout(ly)
        
        self.show()
        
        
app = QApplication(sys.argv) 
reg = registrer()
reg.show()
sys.exit(app.exec_())
