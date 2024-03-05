from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import numpy as np

def compterColonnes(ch):
    nb=0
    for i in range(len(ch)):
        if ch[i]==',':
            nb=nb+1
    return nb+1
def valide(nomF,nbCol):
    v=True
    f=open(nomF,"r")
    ligne=f.readline().strip('\n')
    while ligne!='' and v:
        v=compterColonnes(ligne)==nbCol
        ligne=f.readline().strip('\n')
    return v 
def charger():
    global nbLg,nbCol,titres,T
    
    nbLg=0;nbCol=0;titres=[]
    nomF=w.txtNomFichier.text()
    try:
        
        f=open(nomF,"r")
        ligne1=f.readline().strip('\n')   # permet de lire la 1ère ligne du fichier en ignorant le retour  la ligne
        
        if valide(nomF,compterColonnes(ligne1)):
            nbCol=compterColonnes(ligne1) #détermine le nombre de colonnes suivant la valeur retournée par la fonction
            w.tblDonnees.setColumnCount(nbCol) # fixer le nombre de colonne
            
            ######### determiner les titres de colonnes #####
            ligne1=ligne1+','  # ajout d'une virgule pour faciliter l'extraction
            titres=[]          # tableau vide
            while ligne1.find(',')!=-1:
                titres.append(ligne1[:ligne1.find(',')])  # append permet d'ajouter un élément au tableau(ici le titre de colonne extrait)
                ligne1=ligne1[ligne1.find(',')+1:]        # on efface le titre extrait (y compris la virgule)
            
            w.tblDonnees.setHorizontalHeaderLabels(titres) # fixer les titres de colonnes 
            ####### afficher le reste des infos dans le tableau
            
            ligne=f.readline().strip('\n')      
            while ligne!="":
                nbLg=nbLg+1
                w.tblDonnees.setRowCount(nbLg)
                ligne=ligne+','
                c=0
                while ligne.find(',')!=-1:
                    w.tblDonnees.setItem(nbLg-1,c,QTableWidgetItem(str(ligne[:ligne.find(',')])))
                    ligne=ligne[ligne.find(',')+1:]
                    c=c+1
                ligne=f.readline().strip("\n")
            f.close()
            ######## creation du tableau d'enregistrements 
            e={}
            T=np.array([e]*nbLg)
            chargerVersTableau(T,nbLg)
        else:
            QMessageBox.warning(w,"alert","Format fichier non valide!!")
    except:
        QMessageBox.warning(w,"alert","Fichier introuvable!!")

def chargerVersTableau(T,n):
    global nbCol,titres
    for i in range(n):
        e={}
        for j in range(nbCol):
            e[titres[j]]=w.tblDonnees.item(i,j).text()
        T[i]=e
    
def chargerApartirTalbeau(T,n):
    global nbCol,titres
    w.tblDonnees.clearContents()
    for i in range(n):
        for j in range(nbCol):
            w.tblDonnees.setItem(i,j,QTableWidgetItem(T[i][titres[j]]))
    
def trier(T,n,sens):
    global titres
    arret=False
    while arret==False:
        permut=False
        for i in range (n-1):
            if (sens=="C" and T[i][titres[0]]>T[i+1][titres[0]])or(sens=="D" and T[i][titres[0]]<T[i+1][titres[0]]) :
                aux=T[i]
                T[i]=T[i+1]
                T[i+1]=aux
                permut=True
        arret=permut==False
    
def croissant():
    global nbLg,nbCol,titres,T
    if nbLg==0 or nbCol==0:
        QMessageBox.warning(w,"alert","Rien à trier!!")
    else:
        trier(T,nbLg,"C")
        chargerApartirTalbeau(T,nbLg)
def decroissant():
    global nbLg,nbCol,titres,T
    if nbLg==0 or nbCol==0:
        QMessageBox.warning(w,"alert","Rien à trier!!")
    else:
        trier(T,nbLg,"D")
        chargerApartirTalbeau(T,nbLg)
        
def existe(m,e):
    global titres,nbCol
    trv=False
    i=0
    while trv==False and i<nbCol:
        if e[titres[i]].upper().find(m.upper())!=-1:
            trv=True
        i=i+1
    return trv
def filtrer():
    global T,nbLg
    Tfiltrer=[]
    nb=0
    motRecherche=w.txtFiltrer.text()
    for i in range(nbLg):
        if existe(motRecherche,T[i]):
            Tfiltrer.append(T[i])
            nb=nb+1
    chargerApartirTalbeau(Tfiltrer,nb)
    
            
 
################  PP ##################
nbLg=0    # nb de lignes dans le QTableWidget
nbCol=0   # nb de colonnes dans le QTableWidget
titres=[] # titres de colonnes du QTableWidget
T=[]   # tableau (numpy) d'enregistrements equivalent au QtableWidget


app = QApplication([])
w = loadUi ("interface.ui")
w.show()
w.btnCharger.clicked.connect (charger)
w.btnCroissant.clicked.connect(croissant)
w.btnDecroissant.clicked.connect(decroissant)
w.txtFiltrer.textChanged.connect(filtrer)
app.exec_()