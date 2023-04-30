from copy import *

#%% kataminos


Long=int(input("Long: "))
Large=int(input("large: "))
#Plateau=[[ False for i in range (Large)] for _ in range (Long)]

#LISTE DES PIECES
class Katamino:
    """peut etre pas si utile que ça mais pourquoi pas"""
    def __init__(self, shape, p, sym, max_rot, x_coord=0, y_coord=0):
        self.s=shape
        self.x=x_coord
        self.y=y_coord
        self.priority=p
        self.symmetric=sym
        self.max_r= max_rot

GrandL=Katamino([[True,True],[True,False],[True,False],[True,False]],4, False, 4)
GrandT=Katamino([[True,False],[True,False],[True,False],[True,False]],5, False, 4)
GrandEclair=Katamino([[True,False],[True,False],[True,True],[False,True]],3, False, 4)

GrandV=Katamino([[True,True,True],[True,False,False],[True,False,False]],2, False, 4)

NormalP=Katamino([[True,True],[True,True],[True,False]],6, False, 4)
NormalC=Katamino([[True,True],[True,False],[True,True]],7, True,4)

BizarrdZ=Katamino([[True,False,False],[True,True,True],[False,False,True]],1, False, 2)

IBarre4=Katamino([[True],[True],[True],[True]],8, True, 2)

PetitL=Katamino([[True,True],[True,False],[True,False]],9, False, 4)
PetitT=Katamino([[True,False],[True,True],[True,False]],10, True, 4)
PetitEclair=Katamino([[True,False],[True,True],[False,True]],12,False,2)

Carre=Katamino([[True,True],[True,True]],11,True,1)

IBarre3=Katamino([[True],[True],[True]],13, True,2)
PetitV=Katamino([[True,True],[True,False]],14,False,4)

IBarre2=Katamino([[True],[True]],15,True,2)

Point=Katamino([[True]], 16,True,1)


#ROTATION D'UNE PIECE DE 90°
def tourne90(Piece):
    NPiece=[ [False for i in range (len(Piece.s))] for _ in range (len(Piece.s[0]))]
    for i in range (len(Piece.s)): #Longueur
        for j in range (len(Piece.s[0])): #Largueur
            NPiece[j][i]=Piece.s[len(Piece.s)-1-i][j]
    return NPiece


#SYMETRIE par l'ordonnée
def retourne(Piece):
    p=Piece.s
    NPiece=[ [False for i in range (len(p[0]))] for _ in range (len(p))]
    for i in range (len(p)):
        for j in range (len(p[0])):
            NPiece[i][j]=p[i][len(p[0])-j-1]
    return NPiece

#def ajout_final(Plateau,Liste):0
    



#AJOUT D'UNE PIECE AU PLATEAU

def ajout(Piece,Plateau=[[False for _ in range(Large)] for _ in range (Long)],n=0,m=0):
    Nplateau=Plateau[:]
    for i in range (len(Piece.s)): #colonnes
        for j in range (len(Piece.s[0])): #lignes
            if Piece.s[i][j]:
                if i+n<len(Nplateau) and j+m< len(Nplateau[0]) and (not Nplateau[i+n][j+m]): #(andreas) petite modification pour vérifier que la pièce rentre bien
                    Nplateau[i+n][j+m]=Piece.s[i][j]  #faire un nouveau plateau
                else:
                    return "Erreur"
    return Nplateau

def ajout_final(Piece,Plateau=[[False for _ in range(Large)] for _ in range (Long)],n=0,m=0):
    Nplateau=Plateau[:]
    for i in range (len(Piece.s)): #colonnes
        for j in range (len(Piece.s[0])): #lignes
            if i+n < len(Plateau) and j+m < len(Plateau[0]) and Piece.s[i][j]!=0:
                Nplateau[i+n][j+m]=Piece.priority
            
    return Nplateau
#LEGROS
Liste=[[GrandL,0,0],[IBarre4,0,0],[IBarre3,0,0],[Carre,0,0],[PetitEclair,0,1],[GrandT,1,1]] #[piece,tourne,symetrie,ligne, colonne]

#A LHEURE ACTUELLE (3mars) C4EST APPLIQUE QUI POSE PROBLEME
def applique(Liste,Plateau=[[False for _ in range(Large)] for _ in range (Long)]):
    for i in range (len(Liste)):
        Piece=Liste[i][0]
        Plateau=ajout(Piece,Plateau,Liste[i][0].y,Liste[i][0].x)
    return Plateau

#print(applique(Liste))


#ESSAI PROGRAMME BOURRIN 2

LPieces=[GrandT,GrandL,PetitL,GrandV,Carre,IBarre2]
#pas oublier de def long et large



def bourrin(Liste,Plateau=[[False for _ in range(Large)] for _ in range (Long)]): #,n,m,t,s):
    
    Liste=[deepcopy(a) for a in Liste] #liste des pieces qui restent
    L=Liste[:]
    Listedesdetails=[]
    print(Plateau)
    input()
    if len(L)==0:
        return Plateau,increment
    s,t,i,j=0,0,0,0
    increment = 0
    while len(L)!=0 and increment<150000:
        increment += 1
        rate=True
        print(increment)
        s,t,i,j=0,0,0,0
        if L[0].s==[[True,True],[True,False]]:
            print("ここだよ")
        while s<2 and rate:

            while t<L[0].max_r and rate:
                while j<=len(Plateau[0])-len(L[0].s[0]) and rate:
                    while i<=len(Plateau)-len(L[0].s) and rate: #colonne
                        nP=ajout(L[0],Plateau,i,j)
                        
                        print(L[0].s,nP)
                        if type(nP)!=str:
                            Plateau=nP
                            rate=False
                            if L[0].s==[[True,True],[True,False]]:
                                print(Plateau)
                                input()
                            Listedesdetails.append([L[0],t,s])  #[piece,tourne,symetrie,ligne, colonne]
                            L[0].x,L[0].y=i,j
                            break
                        i+=1
                    i=0
                    j+=1
                j=0

                L[0].s = tourne90(L[0])
                t+=1
            t=0
            L[0].s = retourne(L[0])
            s+=1
        s=0
        print("bip", L[0].x,L[0].y)
        if rate: #si la piece n'est pas posée
                        
            # print('Affichage de la liste des details (avant et après) \n',Listedesdetails) 
            #[piece,tourne,symetrie,ligne, colonne]
            if len(Listedesdetails)==0:
                print("l", [(a.x,a.y) for a in Liste])
                for kata in Liste:
                    ajout_final(kata,Plateau, kata.x, kata.y)
                return Plateau,increment
            s,t,j,i=Listedesdetails[-1][2],Listedesdetails[-1][1],Listedesdetails[-1][0].x,Listedesdetails[-1][0].y
            L=Liste[len(Liste)-len(L)-1:]
            L[0]=Listedesdetails[-1][0]
            if i>len(Plateau)-len(Listedesdetails[-1][0].s):#ptet un pb là
    
                i=0
                if j>len(Plateau[0])-len(Listedesdetails[-1][0].s[0]): #ptet un pb ici
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
#        L[0].x,L[0].y = i,j         
            print("oui", L[0].x, L[0].y)
            Listedesdetails=Listedesdetails[:-1]
            
            Plateau=applique(Listedesdetails)
        else:
            L=L[1:]
        print('\nAffichage du plateau', increment, ' \n',Plateau)

    return (Plateau,increment)


LP2=[NormalP,retourne(GrandEclair),[[6, 0, 6], [6, 6, 6]]] #bon, là ça fonctionne mais jai triché
LP3=[NormalC,GrandEclair,NormalP]
LP3bis=[NormalP,GrandEclair,NormalC]
LP4=[GrandL,PetitT,GrandT,Carre,BizarrdZ,PetitEclair,IBarre3]
LP5=[NormalP,IBarre3,PetitL,PetitT,IBarre4]
LP7=[BizarrdZ,PetitL,PetitV,Carre,Carre,PetitV,NormalP,PetitEclair,PetitV]
print("Katamino bon :\n", bourrin(LP7))