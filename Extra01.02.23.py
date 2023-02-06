#   1-masala
'''from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application")
        self.setGeometry(200,200,500,500)
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",24))
        obj.move(x,y)
    def start(self):
        ok=QPushButton("OK",self)
        self.font(ok,50,50)

        cancel=QPushButton("CANCEL",self)
        self.font(cancel,200,50)

        hbox=QHBoxLayout(self)
        hbox.addStretch()
        hbox.addWidget(ok)
        hbox.addStretch()
        hbox.addWidget(cancel)
        hbox.addStretch()

        vbox=QVBoxLayout(self)
        vbox.addStretch()
        vbox.addWidget(ok)
        vbox.addWidget(cancel)
        vbox.addStretch()

        ok.clicked.connect(self.run)
    def run(self):
        miniwindow=QMessageBox(self)
        miniwindow.setWindowTitle("Xatolar bilan ishlash oynachasi")
        miniwindow.setText("Bu yerda dasturdagi xatolar chiqadi")
        miniwindow.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Reset)
        miniwindow.setDetailedText("Bu yerda xatolik bo'yicha batafsil ma'lumot beriladi")
        miniwindow.setIcon(QMessageBox.Critical)
        miniwindow.setIcon(QMessageBox.Question)
        miniwindow.setIcon(QMessageBox.Information)
        miniwindow.show()
oyna=Window()
oyna.show()
app.exec_()
'''
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Get_Info")
        self.setGeometry(100,100,700,500)
        self.edit()
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",24))
        obj.move(x,y)
    def edit(self):
        t1=QLabel("WRITE: ",self)
        self.font(t1,50,50)
        self.t1=QLineEdit(self)
        self.font(self.t1,200,50)
        miniwindow=QMessageBox(self)
        miniwindow.setWindowTitle("Info_Table")
        if t1==str:
            miniwindow.setText("Bu yerda dasturdagi xatolar chiqadi")
            miniwindow.show()
    def start(self):
        ok=QPushButton("OK",self)
        self.font(ok,280,130)
        ok.clicked.connect(self.edit)
    '''def run(self):
        miniwindow=QMessageBox(self)
        miniwindow.setWindowTitle("Info_Table")
        if self.edit()==str:
            miniwindow.setText("Bu yerda dasturdagi xatolar chiqadi")
            miniwindow.show()
       miniwindow.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Reset)
        miniwindow.setDetailedText("Bu yerda xatolik bo'yicha batafsil ma'lumot beriladi")
        miniwindow.setIcon(QMessageBox.Critical)
        miniwindow.setIcon(QMessageBox.Question)
        miniwindow.setIcon(QMessageBox.Information)'''
        #miniwindow.show()



oyna=Window()
oyna.show()
app.exec_()