import numpy as np
from pickle import load
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

def preparerInterface():
    f=open("villes.txt","r")
    ville=f.readline()[:-1]
    while ville!="":
        w.cmbDe.addItem(ville)
        w.cmbVers.addItem(ville)
        ville=f.readline()[:-1]
    f.close()
def effacerChampsFormulaire():
    w.txtJ.clear()
    w.txtM.clear()
    w.txtA.clear()
    w.txtExp.clear()
    w.txtDest.clear()
    w.cmbDe.setCurrentIndex(0)
    w.cmbVers.setCurrentIndex(0)
    w.txtPoids.clear()
    
def dateValide(j,m,a):
    v=True
    try:
        j=int(j)
        m=int(m)
        a=int(a)
        if j>31 or m>12 or j<1 or m<1 or len(str(a))!=4:
            v=False
        elif m in [4,6,9,11] and j==31:
            v=False
        elif (m==2 and a%4==0 and j>29) or (m==2 and a%4!=0 and j>28):
            v=False      
            
    except:
        v=False
    return v
def poidsValide(reel):
    v=True
    try:
        v= 0<float(reel)<=100
    except:
        v=False
    return v

def chercherKm(dep,arr):
    f=open("distances.bin","rb")
    mat=load(f)
    f.close()
    ####### recherche emplacement ville depart
    trv=False
    i=0; lg=0
    while not(trv) and i<22:
        if mat[i,0]==dep:
            trv=True
            lg=i
        else:
            i=i+1
    ####### recherche emplacement ville arrivee
    trv=False
    j=0;col=0
    while not(trv) and j<22:
        if mat[0,j]==arr:
            trv=True
            col=j
        else:
            j=j+1
    print("dist:",mat[lg,col])
    return mat[lg,col]

def ajouterAuTableau():
    global nbColis
    nbColis=nbColis+1
    w.tblColis.setRowCount(nbColis)
    date=QTableWidgetItem(w.txtJ.text()+"/"+w.txtM.text()+"/"+w.txtA.text())
    exped=QTableWidgetItem(w.txtExp.text())
    dest=QTableWidgetItem(w.txtDest.text())
    de=QTableWidgetItem(w.cmbDe.currentText())
    vers=QTableWidgetItem(w.cmbVers.currentText())
    poids=QTableWidgetItem(w.txtPoids.text())
    if w.chkExpress.isChecked():
        exp=QTableWidgetItem("Oui")
    else:
        exp=QTableWidgetItem("Non")
    km=chercherKm(w.cmbDe.currentText(),w.cmbVers.currentText())
    distance=QTableWidgetItem(km)
    if float(w.txtPoids.text())<1:
        prix=QTableWidgetItem(" 7 Dt")
    else:
        if w.chkExpress.isChecked():
            prix=QTableWidgetItem(str(0.002*float(w.txtPoids.text())*int(km)*1.5)+" Dt")
        else:
            prix=QTableWidgetItem(str(0.002*float(w.txtPoids.text())*int(km))+" Dt")
    w.tblColis.setItem(nbColis-1,0,date)
    w.tblColis.setItem(nbColis-1,1,exped)
    w.tblColis.setItem(nbColis-1,2,dest)
    w.tblColis.setItem(nbColis-1,3,de)
    w.tblColis.setItem(nbColis-1,4,vers)
    w.tblColis.setItem(nbColis-1,5,poids)
    w.tblColis.setItem(nbColis-1,6,exp)
    w.tblColis.setItem(nbColis-1,7,distance)
    w.tblColis.setItem(nbColis-1,8,prix)
    effacerChampsFormulaire()
def controleSaisie():
    if dateValide(w.txtJ.text(),w.txtM.text(),w.txtA.text())==False:
        QMessageBox.warning(w,"Attention","Date invalide!")   
    elif w.txtExp.text()=="":
        QMessageBox.warning(w,"Attention","le champ Expéditeur est vide!")
    elif w.txtDest.text()=="":
        QMessageBox.warning(w,"Attention","le champ Destinataire est vide!")
    elif w.cmbDe.currentText()==w.cmbVers.currentText():
        QMessageBox.warning(w,"Attention","Ville de départ et Ville d'arrivée coincident!")
    elif poidsValide(w.txtPoids.text())==False:
        QMessageBox.warning(w,"Attention","Vérifier le poids du colis!")
    else:
        ajouterAuTableau()                            
    
############### PP ############
nbColis=0
app=QApplication([])
w=loadUi("interface.ui")
preparerInterface()
w.btnAjouter.clicked.connect(controleSaisie)
w.show()
app.exec_()