from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import numpy as np

def afficher():
    w.tbl.setVisible(True)
    taille=int(w.cmbTaille.currentText())
    mat=np.array([[int]*taille]*taille)
    for l in range(taille):
        for c in range(l+1):
            if c==0 or l==c:
                mat[l,c]=1
            else:
                mat[l,c]=mat[l-1,c-1]+mat[l-1,c]
    w.tbl.clear()
    w.tbl.horizontalHeader().setVisible(False)    # masque l'entete horizontal du QTableWidget
    w.tbl.verticalHeader().setVisible(False)      # masque l'entete vertical du QTableWidget
    
    w.tbl.setRowCount(taille)
    w.tbl.setColumnCount(taille)
    for l in range(taille):
        for c in range(l+1):
            w.tbl.setItem(l,c,QTableWidgetItem(str(mat[l,c])))
    
    w.tbl.resizeColumnsToContents()              #ajuste la taille des colonnes au contenu
    w.tbl.resizeRowsToContents()                 #ajuste la taille des lignes au contenu
    w.tbl.setFixedSize(taille*40,taille*24)      #fixe les dimensions (en pixel) du QTableWidget
    
                

##  PP ##

app = QApplication([])
w = loadUi ("interface.ui")
w.tbl.setVisible(False)    # au depart le QTable widget est invisible

w.show()
w.btnAfficher.clicked.connect (afficher)
app.exec_()