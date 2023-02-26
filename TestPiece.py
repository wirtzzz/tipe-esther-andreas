import numpy as np

#XOR ?

#LISTE DES PIECES
# True/False ou 1 / 0 ?
GrandL=[[1,1],[1,0],[1,0],[1,0]]
GrandT=[[1,0],[1,1],[1,0],[1,0]]
GrandEclair=[[1,0],[1,0],[1,1],[0,1]]

GrandV=[[1,1,1],[1,0,0],[1,0,0]]

NormalP=[[1,1],[1,1],[1,0]]
NormalC=[[1,1],[1,0],[1,1]]

BizarrdZ=[[1,0,0],[1,1,1],[0,0,1]]

IBarre4=[[1],[1],[1],[1]]

PetitL=[[1,1],[1,0],[1,0]]
PetitT=[[1,0],[1,1],[1,0]]
PetitEclair=[[1,0],[1,1],[0,1]]

Carre=[[1,1],[1,1]]

IBarre3=[[1],[1],[1]]
PetitV=[[1,1],[1,0]]

IBarre2=[[1],[1]]

Point=[[1]]

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



Long,Large=5,5

#Plateau=[[ False for i in range (Large)] for _ in range (Long)]
Plateau=[np.zeros(Large) for _ in range (Long)]

#AJOUT D'UNE PIECE AU PLATEAU

def ajout(Plateau,Piece,n=0,m=0):

    for i in range (len(Piece)): #lignes
        for j in range (len(Piece[0])): #colonnes
            if Piece[i][j]!=0:
                if Plateau[i+n][j+m]==0:
                    Plateau[i+n][j+m]=Piece[i][j]  #faire un nouveau plateau ou pas?
                else:
                    return "c'est non"
    return Plateau

#LEGROS
Liste=[[np.array(GrandL)*2,0,False,0,3],[np.array(IBarre4)*4,0,False,1,4],[np.array(IBarre3)*4,0,False,0,0],[np.array(Carre)*5,0,False,0,1],[np.array(PetitEclair)*6,1,False,2,0],[np.array(GrandT)*7,1,True,3,0]] #[piece,tourne,symetrie,ligne, colonne]


def applique(Plateau,Liste):
    for i in range (len(Liste)):
        Piece=Liste[i][0]
        if Liste[i][2] :
            Piece=retourne(Piece)
        for _ in range (Liste[i][1]):
            Piece=tourne90(Piece)
        ajout(Plateau,Piece,Liste[i][3],Liste[i][4])
    return Plateau

#patate

def bourrin(Liste,Plateau=[np.zeros(Large) for _ in range (Long)]): #,n,m,t,s):
    
    L=Liste[:]
    if len(L)==0:
        return Plateau
    
    i,j,t,s=0,0,0,0

    while s<2:
        i,j,t=0,0,0
        nP=ajout(Plateau,L[0],i,j)
        if type(nP)!=int:
            return bourrin(L,nP)
        
        while t<4:
            i,j=0,0
            nP=ajout(Plateau,L[0],i,j)
            if type(nP)!=int:
                return bourrin(L,nP)
            
            while j<len(Plateau[0]):
                i=0
                nP=ajout(Plateau,L[0],i,j)
                if type(nP)!=int:
                    return bourrin(L,nP)
                
                while i<len(Plateau):
                    nP=ajout(Plateau,L[0],i,j)
                    if type(nP)!=int:
                        return bourrin(L,nP)
                    i+=1

                j+=1

            tourne90(L[0])
            t+=1

        retourne(L[0])
        s+=1

    return 'T-T'

    

#    retourne tourne90 colonne ligne


print(bourrin(Liste))












