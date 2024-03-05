
import numpy as np

def afficher(taille):
    
    mat=np.array([[int]*taille]*taille)
    ###### remplissage
    for l in range(taille):
        for c in range(l+1):
            if c==0 or l==c:
                mat[l,c]=1
            else:
                mat[l,c]=mat[l-1,c-1]+mat[l-1,c]
    ######## affichage
    for l in range(taille):
        for c in range(l+1):
            print(mat[l,c],end="|")
        print()
    
   
    
                

##  PP ##
taille=int(input("Taille:"))
afficher(taille)
           