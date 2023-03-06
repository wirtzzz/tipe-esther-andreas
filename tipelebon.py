#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      esther
#
# Created:     24/02/2023
# Copyright:   (c) esthe 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import numpy as np



#XOR ?

Long=int(input("Long"))
Large=int(input("large"))
#Plateau=[[ False for i in range (Large)] for _ in range (Long)]
Plateau=[np.zeros(Large) for _ in range (Long)]

#LISTE DES PIECES
# True/False ou 1 / 0 ?
GrandL=[[1,1],[1,0],[1,0],[1,0]]
GrandT=[[2,0],[2,2],[2,0],[2,0]]
GrandEclair=[[3,0],[3,0],[3,3],[0,3]]

GrandV=[[4,4,4],[4,0,0],[4,0,0]]

NormalP=[[5,5],[5,5],[5,0]]
NormalC=[[6,6],[6,0],[6,6]]

BizarrdZ=[[7,0,0],[7,7,7],[0,0,7]]

IBarre4=[[8],[8],[8],[8]]

PetitL=[[9,9],[9,0],[9,0]]
PetitT=[[10,0],[10,10],[10,0]]
PetitEclair=[[11,0],[11,11],[0,11]]

Carre=[[12,12],[12,12]]

IBarre3=[[13],[13],[13]]
PetitV=[[14,14],[14,0]]

IBarre2=[[15],[15]]

Point=[[16]]


#ROTATION D'UNE PIECE DE 90°
def tourne90(Piece):
    NPiece=[ [0 for i in range (len(Piece))] for _ in range (len(Piece[0]))]
    for i in range (len(Piece)): #Longueur
        for j in range (len(Piece[0])): #Largueur
            NPiece[j][i]=Piece[len(Piece)-1-i][j]
    return NPiece


#SYMETRIE par l'ordonnée
def retourne(Piece):
    NPiece=[ [0 for i in range (len(Piece[0]))] for _ in range (len(Piece))]
    for i in range (len(Piece)):
        for j in range (len(Piece[0])):
            NPiece[i][j]=Piece[i][len(Piece[0])-j-1]
    return NPiece




#AJOUT D'UNE PIECE AU PLATEAU

def ajout(Piece,Plateau=[[0 for _ in range(Large)] for _ in range (Long)],n=0,m=0):
    Nplateau=np.copy(Plateau)
    for i in range (len(Piece)): #colonnes
        for j in range (len(Piece[0])): #lignes
            if Piece[i][j]!=0:
                print('nplateau',Nplateau)
                print('piece', Piece)
                if  Nplateau[i+n][j+m]==0: #(andreas) petite modification pour vérifier que la pièce rentre bien
                    Nplateau[i+n][j+m]=Piece[i][j]  #faire un nouveau plateau
                else:
                    return "Erreur"
    return Nplateau


#LEGROS
Liste=[[GrandL,0,0,0,3],[IBarre4,0,0,1,4],[IBarre3,0,0,0,0],[Carre,0,0,0,1],[PetitEclair,0,1,2,0],[GrandT,1,1,3,0]] #[piece,tourne,symetrie,ligne, colonne]

#A LHEURE ACTUELLE (3mars) C4EST APPLIQUE QUI POSE PROBLEME
def applique(Liste,Plateau=[[0 for _ in range(Large)] for _ in range (Long)]):
    for i in range (len(Liste)):
        Piece=Liste[i][0]
        Plateau=ajout(Piece,Plateau,Liste[i][4],Liste[i][3])
    return Plateau

#print(applique(Liste))


#ESSAI PROGRAMME BOURRIN 2

LPieces=[GrandT,GrandL,PetitL,GrandV,Carre,IBarre2]
#pas oublier de def long et large



def bourrin(Liste,Plateau=[[0 for _ in range(Large)] for _ in range (Long)]): #,n,m,t,s):
    L=Liste[:] #liste des pieces qui restent
    Listedesdetails=[]
    if len(L)==0:
        return Plateau
    s,t,i,j=0,0,0,0
    increment = 0
    while len(L)!=0 and increment<20000:
        increment += 1
        rate=True
        while s<2 and rate:

            while t<4 and rate:
                while j<=len(Plateau[0])-len(L[0][0]) and rate:
                    while i<=len(Plateau)-len(L[0]) and rate: #colonne
                        nP=ajout(L[0],Plateau,i,j)
                        
                        if type(nP)!=str:
                            Plateau=nP
                            rate=False
                            Listedesdetails.append([L[0],t,s,j,i])  #[piece,tourne,symetrie,ligne, colonne]
                        print(Listedesdetails,j)
                        i+=1
                    i=0

                    j+=1
                j=0

                L[0] = tourne90(L[0])
                t+=1
            t=0
            L[0] = retourne(L[0])
            s+=1
        s=0
        if rate: #si la piece n'est pas posée
                        
            # print('Affichage de la liste des details (avant et après) \n',Listedesdetails) 
            #[piece,tourne,symetrie,ligne, colonne]
            if len(Listedesdetails)==0:
                return Plateau
            s,t,j,i=Listedesdetails[-1][2],Listedesdetails[-1][1],Listedesdetails[-1][3],Listedesdetails[-1][4]
            L=Liste[len(Liste)-len(L)-1:]
            L[0]=Listedesdetails[-1][0]
            
            if i>len(Plateau)-len(Listedesdetails[-1][0]):#ptet un pb là
                i=0
                if j>len(Plateau[0])-len(Listedesdetails[-1][0][0]): #ptet un pb ici
                    j=0
                    if t>3:
                        t=0
                        if s>0:
                            print("Bizarre2")
                        else:
                            s+=1
                    else:
                        t+=1
                else:
                    j+=1
            else: 
                i+=1
            
            print('jj3',j,'ldd3',Listedesdetails)
            

            Listedesdetails=Listedesdetails[:-1]
            
            Plateau=applique(Listedesdetails)
        else:
            L=L[1:]
        print('\nAffichage du plateau', increment, ' \n',Plateau)

    return Plateau


LP2=[NormalP,retourne(GrandEclair),[[6, 0, 6], [6, 6, 6]]] #bon, là ça fonctionne mais jai triché
LP3=[NormalC,GrandEclair,NormalP]
LP3bis=[NormalP,GrandEclair,NormalC]
LP4=[GrandL,PetitT,GrandT,Carre,BizarrdZ,PetitEclair,IBarre3]
LP5=[NormalP,IBarre3,PetitL,PetitT,IBarre4]
LP7=[NormalP,BizarrdZ,GrandV,GrandL]
print("Katamino bon :\n", bourrin(LP7))