from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, os
from deta import Deta    
        
class main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.stack = QStackedWidget()
        self.stack.addWidget(login(self))
        self.stack.addWidget(registrer(self))
        
        layout = QGridLayout()
        layout.addWidget(self.stack, 0, 0)
        
        self.setLayout(layout)
        self.show()
        
    def login(self):
        self.stack.setCurrentIndex(0)
    
    def registrer(self):
        self.stack.setCurrentIndex(1)
        
class login(QWidget):
    def __init__(self, main, parent=None):
        super().__init__(parent)
        
        llly = QGridLayout()
        
        us = QLabel("Benutzername *")
        self.us1 = QLineEdit()
        ps = QLabel("Passwort *")
        self.ps1 = QLineEdit()
        fe = QPushButton("login")
        pfff = QLabel("* Pflichtfelder")
        rg = QPushButton("registrieren")
        pltz = QLabel()
        
        rg.clicked.connect(main.registrer)
        fe.clicked.connect(self.logii)
        
        llly.addWidget(us, 0, 1)
        llly.addWidget(self.us1, 1, 1)
        llly.addWidget(ps, 2, 1)
        llly.addWidget(self.ps1, 3, 1)
        llly.addWidget(pltz, 4, 1)
        llly.addWidget(fe, 5, 0)
        llly.addWidget(pfff, 5, 1)
        llly.addWidget(rg, 5, 2)
        
        self.setLayout(llly)
        
    def logii(self):
        passwwd = self.ps1.text()
        ussee = self.us1.text()
        deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
        users = deta.Base("user")
        user = users.get(ussee)
        try:
            password = user["passwort"]
            if password == passwwd:
                try:
                    os.remove("user.cvd")
                except:
                    pass
                datei = open("user.cvd", "a")
                datei.write(ussee)
                datei.close()
                msgBox = QMessageBox()
                msgBox.setText("Willkommen zurück, " + ussee)
                msgBox.setInformativeText("Du wurdest erfolgreich angemeldet.")
                msgBox.exec_()
                
            else:
                msgBox = QMessageBox()
                msgBox.setText("41: Du konntest nicht angemeldet werden.")
                msgBox.setInformativeText("Dein Passwort ist falsch. Wenn das Problem weiterhin besteht oder wenn du dein Passwort vergessen hasst, sende uns den Fehlercode per Mail an cows.vs.ducks@gmail.com. Wir senden dir dann dein Passwort an die E-Mail-Adressse, die du bei der Registrierung angegeben hast.")
                msgBox.exec_()
        except:
            msgBox = QMessageBox()
            msgBox.setText("42: Du konntest nicht angemeldet werden.")
            msgBox.setInformativeText("Der Benutzername wurde nicht in unserer Datenbank gefunden. Falls dieser Fehler weiterhin besteht, sende uns den Fehlercode und deinen Benutzernamen per Mail an cows.vs.ducks@gmail.com.")
            msgBox.exec_()

class registrer(QWidget): 
    def __init__(self, main, parent=None): 
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
        log = QPushButton("login")

        fertig.clicked.connect(self.regg)
        log.clicked.connect(main.login)
        
        ly.addWidget(fertig, 8, 0)
        ly.addWidget(pf, 8, 1)
        ly.addWidget(log, 8, 2)
        
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
            try:
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
                              "waffen": "1",
                              "tränke": "False",
                              "status": "gamer"
                })
            except:
                msgBox = QMessageBox()
                msgBox.setText("40: Du konntest nicht registriert werden.")
                msgBox.setInformativeText("Stelle sicher, dass du mit dem Internet verbunden bist. Wenn ja, ist der Benutzername schon vergeben. Wenn das Problem weiterhin besteht , sende uns den Fehlercode und den Benutzernamen, den du haben willst per Mail an cows.vs.ducks@gmail.com.")
                msgBox.exec_()
        
            msgBoxr = QMessageBox()
            msgBoxr.setText("Du wurdest erfolgreich registriert.")
            msgBoxr.exec_()
            
            sys.exit()
            
        else:
            msgBox = QMessageBox()
            msgBox.setText("43: Du konntest nicht registriert werden.")
            msgBox.setInformativeText("Vielleicht hast du das Passwort nicht korrekt wiederholt oder du hast nicht alle Pflichtfelder ausgefüllt. Wenn alles stimmt, und dieser Fehler weiterhin auftritt, sende uns den Gehlercode per Mail an cows.vs.ducks@gmail.com.")
            msgBox.exec_()
        
        
app = QApplication(sys.argv) 
reg = main()
reg.show()
sys.exit(app.exec_())
