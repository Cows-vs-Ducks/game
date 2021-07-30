from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
import sys, os, time, random

class Hearth(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ly = QGridLayout()

        self.bothearth1 = QSvgWidget("heart.svg", self)
        self.bothearth1.setFixedSize(50, 50)
        ly.addWidget(self.bothearth1, 0, 7)

        self.bothearth2 = QSvgWidget("heart.svg", self)
        self.bothearth2.setFixedSize(50, 50)
        ly.addWidget(self.bothearth2, 0, 8)

        self.bothearth3 = QSvgWidget("heart.svg", self)
        self.bothearth3.setFixedSize(50, 50)
        ly.addWidget(self.bothearth3, 0, 9)

        platzhalter = QLabel()
        ly.addWidget(platzhalter, 0, 4)

        self.userhearth1 = QSvgWidget("heart.svg", self)
        self.userhearth1.setFixedSize(50, 50)
        ly.addWidget(self.userhearth1, 0, 1)

        self.userhearth2 = QSvgWidget("heart.svg", self)
        self.userhearth2.setFixedSize(50, 50)
        ly.addWidget(self.userhearth2, 0, 2)

        self.userhearth3 = QSvgWidget("heart.svg", self)
        self.userhearth3.setFixedSize(50, 50)
        ly.addWidget(self.userhearth3, 0, 3)

        self.herrbot = 3
        self.herruser = 3

        self.setLayout(ly)
        self.show()

    def lesshearthbot(self):
        if self.herruser == 3:
            self.bothearth3.move(1000000, 1000000)
            self.herruser = 2
        elif self.herruser == 2:
            self.bothearth2.move(1000000, 1000000)
            self.herruser = 1
        elif self.herruser == 1:
            self.bothearth1.move(1000000, 1000000)
            msgbox = QMessageBox()
            msgbox.setText("Du hast Gewonnen!!!")
            msgbox.setWindowTitle("Gewonnen")
            msgbox.exec()
            sys.exit()


    def lesshearthuser(self):
        if self.herrbot == 3:
            self.userhearth3.move(1000000, 1000000)
            self.herrbot = 2
        elif self.herrbot == 2:
            self.userhearth2.move(1000000, 1000000)
            self.herrbot = 1
        elif self.herrbot == 1:
            self.userhearth1.move(1000000, 1000000)
            msgbox = QMessageBox()
            msgbox.setText("Du hast leider verloren. Probiere es doch einfach nochmal!")
            msgbox.setWindowTitle("Verloren")
            msgbox.exec()
            sys.exit()

class Svg(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ly = QHBoxLayout()
        self.hearthh = Hearth()
        ly.addWidget(self.hearthh)

        fileh1 = open("height.cvd", "r")
        self.height = fileh1.read()
        fileh1.close()
        filew1 = open("width.cvd", "r")
        self.width = filew1.read()
        filew1.close()

        self.actutime = 4
        #self.herr = 3
        
        self.ball = QWidget(self)
        self.ball.setStyleSheet("background-color:black;border-radius:25px")
        self.ball.resize(50, 50)
        self.ball.move(1000000, 1000000)

        self.botball = QWidget(self)
        self.botball.setStyleSheet("background-color:black;border-radius:25px")
        self.botball.resize(50, 50)
        self.botball.move(1000000, 1000000)
        
        self.botzu = random.randint(0, 10)
        self.boti = 0
        
        self.stepw = int(self.width) / 20
        self.steph = int(self.height) / 15
        
        self.keyUp = "16777235"
        self.keyDown = "16777237"
        self.keyLeft = "16777234"
        self.keyRight = "16777236"
        
        self.cowx = 0
        self.cowy = int(self.height) / 2
        self.duckx = int(self.width) - 200
        self.ducky = int(self.height) / 2

        self.waffe = "1"
        
        self.pic = QSvgWidget("cow.svg", self) # Cow
        self.pic.setFixedSize(175, 200)
        self.pic.move(self.cowx, self.cowy)
        
        self.pic2 = QSvgWidget("cow.svg", self) # Duck
        self.pic2.setFixedSize(175, 200)
        self.pic2.move(self.duckx, self.ducky)
        
        self.botshoot = QTimer()
        self.botshoot.timeout.connect(self.shootbot)
        self.botshoot.start(4000)
        
        self.setLayout(ly)
        self.setGeometry(0, 0, int(self.width), int(self.height))
        self.show()

    def closeEvent(self, event):
        msgbox = QMessageBox()
        msgbox.setText("Bist du sicher, dass du das Spiel abbrechen willst?")
        msgbox.setWindowTitle("Abbrechen?")
        msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        rv = msgbox.exec()
        if rv == QMessageBox.Cancel:
            event.ignore()
        else:
            event.accept()
        
    def keyPressEvent(self, event):
        if str(event.key()) == self.keyRight:
            self.right()
        elif str(event.key()) == self.keyDown:
            self.down()
        elif str(event.key()) == self.keyLeft:
            self.left()
        elif str(event.key()) == self.keyUp:
            self.up()
        else:
            pass
        
        event.accept()

    def mousePressEvent(self, event):
        self.shootx = event.x()
        self.shooty = event.y()
        self.timer = QTimer()
        #self.timer.timeout.connect(self.botaus)
        #self.timer.setSingleShot(True)
        #self.timer.start(1000)
        self.shootuser()
        self.botaus()
        event.accept()
        
    def botaus(self):
        if self.boti >= self.botzu:
            self.botzu = random.randint(0, 10)
            self.boti = 0
        else:
            if self.shootx <= self.duckx + 175 and self.shooty <= self.ducky + 200 and self.shootx >= self.duckx and self.shooty >= self.ducky:
                for x in range(0, 4):
                    self.botup()
            
                self.timer = QTimer()
                self.timer.timeout.connect(self.botback)
                self.timer.setSingleShot(True)
                self.timer.start(2000)
                self.boti += 1
            
            else:
                pass
    
    def botback(self):
        for x in range(0, 4):
            self.botdown()

    def botdown(self):
        self.ducky += self.steph
        self.duckx = self.duckx
        self.pic2.move(self.duckx, self.ducky)
        
    def botup(self):
        self.ducky -= self.steph
        self.duckx = self.duckx
        self.pic2.move(self.duckx, self.ducky)
        
    def checkuser(self):
        if self.shootx <= self.duckx + 175 and self.shooty <= self.ducky + 200 and self.shootx >= self.duckx and self.shooty >= self.ducky:
            print("getroffen")
            self.ball.move(1000000, 1000000)
            self.hearthh.lesshearthbot()
        else:
            self.ball.move(1000000, 1000000)

    def checkbot(self):
        if self.shootx <= self.cowx + 175 and self.shooty <= self.cowy + 200 and self.shootx >= self.cowx and self.shooty >= self.cowy:
            print("getroffen")
            self.ball.move(1000000, 1000000)
            self.hearthh.lesshearthuser()
        else:
            self.ball.move(1000000, 1000000)

    def shootuser(self):
        user = "user"
        if user == "user":
            if self.actutime - time.time() >= 3 or self.actutime == 4:
                if self.waffe == "1":
                    self.shootanim = QPropertyAnimation(self.ball, b"pos")
                    self.shootanim.setDuration(1000)
                    self.shootanim.setStartValue(QPoint(self.cowx, self.cowy))
                    self.shootanim.setEndValue(QPointF(self.shootx, self.shooty))
                    self.shootanim.start()
                    self.timer = QTimer()
                    self.timer.timeout.connect(self.checkuser)
                    self.timer.setSingleShot(True)
                    self.timer.start(1000) 
                    self.actutume = time.time()
            else:
                pass

    def shootbot(self):
        self.shootx = self.cowx + 25
        self.shooty = self.cowy + 25
        self.shootanim = QPropertyAnimation(self.botball, b"pos")
        self.shootanim.setDuration(1000)
        self.shootanim.setStartValue(QPoint(self.duckx, self.ducky))
        self.shootanim.setEndValue(QPointF(self.shootx, self.shooty))
        self.shootanim.start()
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkbot)
        self.timer.setSingleShot(True)
        self.timer.start(1000) 
        self.actutume = time.time()
        
    def right(self):
        self.cowx += self.stepw
        self.cowy = self.cowy
        self.pic.move(self.cowx, self.cowy)
    
    def down(self):
        self.cowy += self.steph
        self.cowx = self.cowx
        self.pic.move(self.cowx, self.cowy)
    
    def left(self):
        self.cowx -= self.stepw
        self.cowy = self.cowy
        self.pic.move(self.cowx, self.cowy)
    
    def up(self):
        self.cowy -= self.steph
        self.cowx = self.cowx
        self.pic.move(self.cowx, self.cowy)

app = QApplication([])
try:
    os.remove("width.cvd")
    os.remove("height.cvd")
except:
    pass
filew = open("width.cvd", "a")
filew.write(str(app.desktop().width()))
filew.close()
fileh = open("height.cvd", "a")
fileh.write(str(app.desktop().height()))
fileh.close()
svg = Svg()
svg.setWindowTitle("Cows vs. Ducks")
svg.setWindowIcon(QIcon("cvd-icon.png"))
svg.show()
sys.exit(app.exec_())