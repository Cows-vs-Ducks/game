from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
import sys, os, time

class Svg(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ly = QHBoxLayout()

        fileh1 = open("height.cvd", "r")
        self.height = fileh1.read()
        fileh1.close()
        filew1 = open("width.cvd", "r")
        self.width = filew1.read()
        filew1.close()

        self.ball = QWidget(self)
        self.ball.setStyleSheet("background-color:black;border-radius:25px")
        self.ball.resize(50, 50)
        
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
        
        self.pic = QSvgWidget("cow.svg", self) # Cow
        self.pic.setFixedSize(175, 200)
        self.pic.move(self.cowx, self.cowy)
        
        self.pic2 = QSvgWidget("cow.svg", self) # Duck
        self.pic2.setFixedSize(175, 200)
        self.pic2.move(self.duckx, self.ducky)
        
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
        self.shoot("user") # this is the user and not the bot
    
    def checkuser(self):
        if self.shootx <= self.duckx + 175 and self.shooty <= self.ducky + 200 and self.shootx >= self.duckx and self.shooty >= self.ducky:
            print("getroffen")

    def shoot(self, user):
        self.shootanim = QPropertyAnimation(self.ball, b"pos")
        self.shootanim.setDuration(1000)
        self.shootanim.setStartValue(QPoint(self.cowx, self.cowy))
        self.shootanim.setEndValue(QPointF(self.shootx, self.shooty))
        self.shootanim.start()
        self.timer = QTimer()
        if user == "user":
            self.timer.timeout.connect(self.checkuser)
        elif user == "bot":
            user
        else:
            pass
        self.timer.setSingleShot(True)
        self.timer.start(1000) 
        
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