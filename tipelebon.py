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
    # print("Pièce avant rotation 90°", Piece)
    NPiece=[ [0 for i in range (len(Piece))] for _ in range (len(Piece[0]))]
    for i in range (len(Piece)): #Longueur
        for j in range (len(Piece[0])): #Largueur
            NPiece[j][i]=Piece[len(Piece)-1-i][j]
    # print("Pièce avant rotation 90°", Piece)
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
                if Nplateau[i+n][j+m]==0:
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
        if Liste[i][1]==1 :
            Piece=retourne(Piece)
        for _ in range (Liste[i][2]):
            Piece=tourne90(Piece)
        Plateau=ajout(Piece,Plateau,Liste[i][4],Liste[i][3])
    return Plateau

#print(applique(Liste))


#ESSAI PROGRAMME BOURRIN 2

LPieces=[GrandT,GrandL,PetitL,GrandV,Carre,IBarre2]
#pas oublier de def long et large



def bourrin(Liste,Plateau=[[0 for _ in range(Large)] for _ in range (Long)]): #,n,m,t,s):
    print('\nListe des pièces \n:',Liste)
    L=Liste[:] #liste des pieces qui restent
    Listedesdetails=[]
    if len(L)==0:
        return Plateau
    ss,tt,ii,jj=0,0,0,0
    increment = 0
    while len(L)!=0 and increment<200000:
        increment += 1
        rate=True
        s=ss
        while s<2 and rate:
            t=tt

            while t<4 and rate:
                j=jj
                while j<=len(Plateau[0])-len(L[0][0]) and rate:#ligne
                    i=ii #ce qui est bizarre c'est que dans LP3bis 6 ne retourne pas en haut à gauche donc pb avec j
                    while i<=len(Plateau)-len(L[0]) and rate: #colonne
                        #print('ldd av ap',Listedesdetails,'j',j)
                        nP=ajout(L[0],Plateau,i,j)
                        
                        if type(nP)!=str:
                            
                            Plateau=nP
                            rate=False
                            Listedesdetails.append([L[0],s,t,j,i])  #[piece,tourne,symetrie,ligne, colonne]

                        i+=1
                    ii=0

                    j+=1
                jj=0

                L[0] = tourne90(L[0])
                t+=1
            tt=0
            L[0] = retourne(L[0])
            s+=1
        ss=0
        if rate: #si la piece n'est pas posée
            
            id=-1 #le dernier élément de la liste (comme rate est vraie, il s'agit de l'élément d'avant
            
            # print('Affichage de la liste des details (avant et après) \n',Listedesdetails) 
            #[piece,tourne,symetrie,ligne, colonne]
            if len(Listedesdetails)==0:
                return Plateau
            
            ss,tt,jj,ii=Listedesdetails[id][1],Listedesdetails[id][2],Listedesdetails[id][3],Listedesdetails[id][4]

            #Si on sort du plateau, on passe à la position suivante
            Piecor=Listedesdetails[id][0] #piece orientée
            for _ in range (tt):
                Piecor=tourne90(Piecor)
            if ss>0:
                Piecor=retourne(Piecor)
            if ss>1:
                return 'attention'
            
            if ii>len(Plateau)-len(Piecor):#ptet un pb là
                ii=0
                if jj>len(Plateau[0])-len(Piecor[0]): #ptet un pb ici
                    jj=0
                    if tt+1>3:
                        tt=0
                        if ss>0:
                            return "Bizarre2"
                        else:
                            ss+=1
                    else:
                        tt+=1
                else:
                    jj+=1
            else: 
                ii+=1
            
            if ss>1:
                return 'attention2'
                
            #SS ET II SONT BIZARREs DANS LISTEDESDETAILS!!!!!
            #print('ldd',Listedesdetails)
            print('ss1',ss,'tt',tt,'\nLdd\n',Listedesdetails)
            Listedesdetails=Listedesdetails[:-1]#jenleve le dernier element
            # print('\n', Listedesdetails)
            
            # print('\nAffichage de L si rate (avant et après ajout) \n',L)
            L=Liste[len(Liste)-len(L)-1:]
            # print('\n',L)
            for _ in range (tt):
                L[0]=tourne90(L[0])
            if ss==1:
                L[0]=retourne(L[0])
            #print('L[0]',L[0])
            print('ss2',ss,'tt',tt,'\nLdd\n',Listedesdetails)

            #print('jj3',jj,'ldd3',Listedesdetails)
            
            # print('Affichage du plateau (avant et après) \n',Plateau)
            Plateau=applique(Listedesdetails) #le Plateau sans les 2 derniers éléments
            # print('\n',Plateau)
        else:
            #print('\nAffichage de L si réussi (avant et après suppression) \n',L)
            L=L[1:]
            #print('\n',L)
        print('\nAffichage du plateau', increment, ' \n',Plateau)
    return Plateau


LP2=[NormalP,retourne(GrandEclair),[[6, 0, 6], [6, 6, 6]]] #bon, là ça fonctionne mais jai triché
LP3=[NormalC,GrandEclair,NormalP]
LP3bis=[NormalP,GrandEclair,NormalC]
LP4=[GrandL,PetitT,GrandT,Carre,BizarrdZ,PetitEclair,IBarre3]
LP5=[NormalP,IBarre3,PetitL,PetitT,IBarre4]#4,5 fonctionne mais pas 5,4 

print("Katamino bon :\n", bourrin(LP5))

