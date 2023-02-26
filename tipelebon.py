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

##def ajout2(Piece,Plateau=[np.zeros(Large) for _ in range (Long)],n=0,m=0):
##    for i in range (len(Piece)): #lignes
##        for j in range (len(Piece[0])): #colonnes
##            if Piece[i][j]!=0:
##                print('i',i,'j',j,'n',n,'m',m)
##                if Plateau[i+n][j+m]==0:
##                    Plateau[i+n][j+m]=Piece[i][j]  #ne pas faire un nouveau plateau
##                else:
##                    return "c'est non"
##    return Plateau

def ajout(Piece,Plateau=[np.zeros(Large) for _ in range (Long)],n=0,m=0):
    Nplateau=np.copy(Plateau)
    for i in range (len(Piece)): #colonnes
        for j in range (len(Piece[0])): #lignes
            if Piece[i][j]!=0:
                if Nplateau[i+n][j+m]==0:
                    Nplateau[i+n][j+m]=Piece[i][j]  #faire un nouveau plateau
                else:
                    return "c'est non"
    return Nplateau


#LEGROS
Liste=[[GrandL,0,0,0,3],[IBarre4,0,0,1,4],[IBarre3,0,0,0,0],[Carre,0,0,0,1],[PetitEclair,1,0,2,0],[GrandT,1,1,3,0]] #[piece,tourne,symetrie,ligne, colonne]


def applique(Liste,Plateau=[np.zeros(Large) for _ in range (Long)]):
    for i in range (len(Liste)):
        Piece=Liste[i][0]
        if Liste[i][2]==1 :
            Piece=retourne(Piece)
        for _ in range (Liste[i][1]):
            Piece=tourne90(Piece)
        ajout(Piece,Plateau,Liste[i][3],Liste[i][4])
    return Plateau

#ESSAI PROGRAMME BOURRIN 2

LPieces=[GrandT,GrandL,PetitL,GrandV,Carre,IBarre2]
#pas oublier de def long et large



def bourrin(Liste,Plateau=[np.zeros(Large) for _ in range (Long)]): #,n,m,t,s):

    L=Liste[:]
    Listedesdetails=[]
    if len(L)==0:
        return Plateau
    a,b,c,d=0,0,0,0

    while len(L)!=0:

        truc=True
        i,j,t,s=a,b,c,d
        while s<2 and truc:

            i,j,t=b,c,d

            while t<4 and truc:

                i,j=c,d

                while j<len(Plateau[0])-len(L[0][0])+1 and truc:#ligne
                    i=d
                    while i<len(Plateau)-len(L[0])+1 and truc: #colonne
                        nP=ajout(L[0],Plateau,i,j)

                        if type(nP)!=str:
                            Plateau=nP
                            truc=False
                            Listedesdetails.append([L[0],t,s,j,i])  #[piece,tourne,symetrie,ligne, colonne]
                        i+=1
                        d=0

                    j+=1
                    c=0

                tourne90(L[0])
                t+=1
                b=0
            retourne(L[0])
            s+=1
        a=0
        if truc: #si la piece n'est pas posée
            print(Listedesdetails,Listedesdetails[-1][2])
            id=-1 #le dernier élément de la liste (comme true est vraie, il s'agit de l'élément d'avant
            ##print(id)
            a,b,c,d=Listedesdetails[id][2],Listedesdetails[id][1],Listedesdetails[id][3],Listedesdetails[id][4]+1
            Listedesdetails=Listedesdetails[:-1]
            L=Liste[len(Liste)-len(L)-1:] #jenleve le dernier element
            print('1',Plateau)
            Plateau=applique(Listedesdetails) #le Plateau sans les 2 derniers éléments
            print('2',Plateau)
        else:
            L=L[1:]
            print(L)
    return Plateau,Listedesdetails


LP2=[NormalP,retourne(GrandEclair),[[6, 0, 6], [6, 6, 6]]] #bon, là ça fonctionne mais jai triché
LP3=[NormalP,GrandEclair,NormalC]


print(bourrin(LP3))

