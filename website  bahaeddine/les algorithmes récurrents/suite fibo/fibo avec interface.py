from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


def fibo(n):
    u0=1
    u1=1
    for i in range(2,n+1):
        u=u1+u0
        u0=u1
        u1=u
    return u
def plus():
    w.txtTerme.setText(str(int(w.txtTerme.text())+1))
def moins():
    if int(w.txtTerme.text())>=1:
        w.txtTerme.setText(str(int(w.txtTerme.text())-1))
    else:
         w.txtTerme.setText("0")
        
def maj():
    n=w.txtTerme.text()
    w.lblAff.setText("U"+n+"="+str(fibo(int(n))))
##  Votre code içi ##

app = QApplication([])
w = loadUi ("interface.ui")
w.show()
w.btnPlus.clicked.connect (plus)
w.btnMoins.clicked.connect (moins)
w.txtTerme.textChanged.connect(maj)
app.exec_()






######### PP ##########
n=int(input("Quel terme calculer?:"))
print("U"+str(n)+"=",fibo(n))
