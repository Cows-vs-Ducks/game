from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from deta import Deta    
        
class main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.stack = QStackedWidget()
        self.stack.addWidget(login())
        self.stack.addWidget(registrer())
        
        page1Button = QPushButton("Page 1")
        page2Button = QPushButton("Page 2")
        page1Button.clicked.connect(self.setPage1)
        page2Button.clicked.connect(self.setPage2)
    
        layout = QGridLayout()
        layout.addWidget(self.stack, 0, 0)
        layout.addWidget(page1Button, 1, 0)
        layout.addWidget(page2Button, 1, 1)
        
        self.setLayout(layout)
        self.show()
        
    def setPage1(self):
        self.stack.setCurrentIndex(0)
    
    def setPage2(self):
        self.stack.setCurrentIndex(1)
        
class login(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        llly = QGridLayout()
        
        us = QLabel("Benutzername *")
        us1 = QLineEdit()
        ps = QLabel("Passwort *")
        ps1 = QLineEdit()
        fe = QPushButton("login")
        pltz = QLabel()
        llly.addWidget(us, 0, 0)
        llly.addWidget(us1, 1, 0)
        llly.addWidget(ps, 2, 0)
        llly.addWidget(ps1, 3, 0)
        llly.addWidget(pltz, 4, 0)
        llly.addWidget(fe, 5, 0)
        
        self.setLayout(llly)

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
                          "waffen": "standart",
                          "status": "gamer"
            })
            msgBoxr = QMessageBox()
            msgBoxr.setText("Du wurdest erfolgreich registriert.")
            msgBoxr.exec_()
            
            sys.exit()
            
        else:
            msgBox = QMessageBox()
            msgBox.setText("43: Du konntest nicht registriert werden.")
            msgBox.setInformativeText("Vielleicht hast du das Passwort nicht korrekt wiederholt oder du hast nicht alle Pflichtfelder ausgefüllt. Wenn alles stimmt, und dieser Fehler weiterhin auftritt, gehe auf cows-vs-ducks.tk und schreibe uns über den Chat den Fehlercode.")
            msgBox.exec_()
        
        
app = QApplication(sys.argv) 
reg = main()
reg.show()
sys.exit(app.exec_())
