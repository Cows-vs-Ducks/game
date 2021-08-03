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
          
        
app = QApplication(sys.argv) 
reg = main()
reg.show()
sys.exit(app.exec_())
