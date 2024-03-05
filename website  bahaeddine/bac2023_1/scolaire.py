from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import dump ,load
from numpy import*
def annuler():
    w.c1.clear()
    w.n1.clear()
    w.m1.clear()
    w.l1.clear()
    w.d1.clear()
    w.m1.clear()
    w.a1.clear()
    w.r1.clear()
    
def ajouter():
    e=dict(cin=str,np=str,gr=str,sec=str,moy=float,opt=str)
    e["cin"]=w.c1.text()
    e["np"]=w.n1.text()
    if w.h1.isChecked():
        e["gr"]="Homme"
    else:
        e["gr"]="femme"
    e["sec"]=w.l1.currentText()
    e["moy"]=float(w.m1.text())
    if w.d1.isChecked():
        e["opt"]="Dessan"
    else:
        e["opt"]="musique"
    if (e["opt"]==""):
        QMessageBox.critical(w,"Erreur","cocher l'option")
    else:
        f=open("eleves.dat","ab")
        dump(e,f)
        f.close()
        QMessageBox.information(w,"info","eleve ajouter avec secces")
def taille ():
    f=open("eleves.dat","rb")
    n=0
    ok=True
    while ok :
        try:
            e=load(f)
            n=n+1
        except:
            ok=False
    f.close()
    return n
        

def afficher():
    n=taille()
    t=array([dict()]*n)
    f=open("eleves.dat","rb")
    for i in range (n):
        t[i]=load(f)
    f.close()
    ok=True
    while ok:
        ok=False
        for i in range (0,n-1):
            if  t[i]["moy"]< t[i+1]["moy"]:
                aux=t[i]
                t[i]=t[i+1]
                t[i+1]=aux
                ok=True
    f=open("eleves.dat","wb")
    for i in range (n):
        dump(t[i],f)
    f.close()
    w.tab.setRowCount(n)
    w.tab.setColumnCount(4)
    f=open("eleves.dat","rb")
    for i in range(n):
        e=load(f)
        w.tab.setItem(i,0,QTableWidgetItem(str(i+1)))
        w.tab.setItem(i,1,QTableWidgetItem((e["cin"])))
        w.tab.setItem(i,2,QTableWidgetItem(e["np"]))
        w.tab.setItem(i,3,QTableWidgetItem(str(e["moy"])))
    f.close()

def calculer():
    n=taille()
    nb=0
    f=open("eleves.dat","rb")
    for i in range (n):
        e=load(f)
        nb=nb+1
    f.close()
    pa=(str(nb/n)*100)
    w.a1.setText(str(pa))
    w.r1.setText(str(100-pa))
    
    
    
    
    

    





app=QApplication([])
w=loadUi("scolaire.ui")
w.b1.clicked.connect(ajouter)
w.b2.clicked.connect(annuler)
w.b3.clicked.connect(afficher)
w.ca.clicked.connect(calculer)

w.show()
app.exec_()