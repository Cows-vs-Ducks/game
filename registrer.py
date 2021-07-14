from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from deta import Deta

class registrer(QWidget): 
    def __init__(self, parent=None): 
        super().__init__(parent)
        
        ly = QGridLayout()
        
        lvn = QLabel("Vorname")
        self.vn = QLineEdit()
        lnn = QLabel("Nachname")
        self.nn = QLineEdit()
        lag = QLabel("Alter")
        self.ag = QLineEdit()
        lgb = QLabel("Geburtsdatum (tt.mm.jjjj)")
        self.gb = QLineEdit()
        
        lus = QLabel("Benutzername *")
        self.us = QLineEdit()
        lem = QLabel("E-Mail-Adresse *")
        self.em = QLineEdit()
        lps = QLabel("Passwort *")
        self.ps = QLineEdit()
        lpss = QLabel("Passwort wiederholen *")
        self.pss = QLineEdit()
        
        fertig = QPushButton("registrieren")
        pf = QLabel("* Pflichtfelder")

        fertig.clicked.connect(self.regg)
        
        ly.addWidget(fertig, 8, 1)
        ly.addWidget(pf, 8, 2)
        
        ly.addWidget(lvn, 0, 0)
        ly.addWidget(self.vn, 1, 0)
        ly.addWidget(lnn, 2, 0)
        ly.addWidget(self.nn, 3, 0)
        ly.addWidget(lag, 4, 0)
        ly.addWidget(self.ag, 5, 0)
        ly.addWidget(lgb, 6, 0)
        ly.addWidget(self.gb, 7, 0)
        
        ly.addWidget(lus, 0, 3)
        ly.addWidget(self.us, 1, 3)
        ly.addWidget(lem, 2, 3)
        ly.addWidget(self.em, 3, 3)
        ly.addWidget(lps, 4, 3)
        ly.addWidget(self.ps, 5, 3)
        ly.addWidget(lpss, 6, 3)
        ly.addWidget(self.pss, 7, 3)
        
        self.setLayout(ly)
        
        self.show()

    def regg(self):
        vn = self.vn.text()
        nn = self.nn.text()
        ag = self.ag.text()
        gb = self.gb.text()
        us = self.us.text()
        em = self.em.text()
        ps = self.ps.text()
        pss = self.pss.text()

        if em != "" and em != "" and ps != "" and pss == ps:
            deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
            users = deta.Base("user")
            users.insert({"key": us,
                          "vorname": vn,
                          "nachname": nn,
                          "alter": ag,
                          "geburtsdatum": gb,
                          "benutzername": us,
                          "email": em,
                          "passwort": ps,
                          "moneten": "0",
                          "level": "1",
                          "waffen": "standart"
            })
            
        else:
            msgBox = QMessageBox()
            msgBox.setText("Du konntest nicht registriert werden. Vielleicht hast du das Passwort nicht korrekt wiederholt oder du hast nicht alle Pflichtfwlder ausgefüllt. Wenn alles stimmt, und dieser Fehler immer noch kommet, gehe auf cows-vs-ducks.tk und schreibe uns über den Chat den Fehlercode 43.")
            msgBox.exec_()
        
        
app = QApplication(sys.argv) 
reg = registrer()
reg.show()
sys.exit(app.exec_())
