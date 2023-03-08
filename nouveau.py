from copy import *

#%% kataminos


Long=int(input("Long: "))
Large=int(input("large: "))
#Plateau=[[ False for i in range (Large)] for _ in range (Long)]

#LISTE DES PIECES
# True/False ou 1 / 0 ?
class Katamino:
    """peut etre pas si utile que ça mais pourquoi pas"""
    def __init__(self, shape, p, x_coord=0, y_coord=0):
        self.s=shape
        self.x=x_coord
        self.y=y_coord
        self.priority=p


GrandL=Katamino([[True,True],[True,False],[True,False],[True,False]],4)
GrandT=Katamino([[True,False],[True,False],[True,False],[True,False]],5)
GrandEclair=Katamino([[True,False],[True,False],[True,True],[False,True]],3)

GrandV=Katamino([[True,True,True],[True,False,False],[True,False,False]],2)

NormalP=Katamino([[True,True],[True,True],[True,False]],6)
NormalC=Katamino([[True,True],[True,False],[True,True]],7)

BizarrdZ=Katamino([[True,False,False],[True,True,True],[False,False,True]],1)

IBarre4=Katamino([[True],[True],[True],[True]],8)

PetitL=Katamino([[True,True],[True,False],[True,False]],9)
PetitT=Katamino([[True,False],[True,True],[True,False]],10)
PetitEclair=Katamino([[True,False],[True,True],[False,True]],12)

Carre=Katamino([[True,True],[True,True]],11)

IBarre3=Katamino([[True],[True],[True]],13)
PetitV=Katamino([[True,True],[True,False]],14)

IBarre2=Katamino([[True],[True]],15)

Point=Katamino([[True]], 16)


#ROTATION D'UNE PIECE DE 90°
def tourne90(Piece):
    p=Piece.s
    NPiece=[ [0 for i in range (len(p))] for _ in range (len(p[0]))]
    for i in range (len(p)): #Longueur
        for j in range (len(p[0])): #Largueur
            NPiece[j][i]=p[len(p)-1-i][j]
    return NPiece


#SYMETRIE par l'ordonnée
def retourne(Piece):
    p=Piece.s
    NPiece=[ [0 for i in range (len(p[0]))] for _ in range (len(p))]
    for i in range (len(p)):
        for j in range (len(p[0])):
            NPiece[i][j]=p[i][len(p[0])-j-1]
    return NPiece




#AJOUT D'UNE PIECE AU PLATEAU

def ajout(Piece,Plateau=[[0 for _ in range(Large)] for _ in range (Long)],n=0,m=0):
    Nplateau=Plateau[:]
    for i in range (len(Piece.s)): #colonnes
        for j in range (len(Piece.s[0])): #lignes
            if Piece.s[i][j]!=0:
                print('nplateau',Nplateau)
                if  Nplateau[i+n][j+m]==0: #(andreas) petite modification pour vérifier que la pièce rentre bien
                    Nplateau[i+n][j+m]=Piece.s[i][j]  #faire un nouveau plateau
                else:
                    return "Erreur"
    return Nplateau


#LEGROS
Liste=[[GrandL,0,0],[IBarre4,0,0],[IBarre3,0,0],[Carre,0,0],[PetitEclair,0,1],[GrandT,1,1]] #[piece,tourne,symetrie,ligne, colonne]

#A LHEURE ACTUELLE (3mars) C4EST APPLIQUE QUI POSE PROBLEME
def applique(Liste,Plateau=[[0 for _ in range(Large)] for _ in range (Long)]):
    for i in range (len(Liste)):
        Piece=Liste[i][0]
        Plateau=ajout(Piece,Plateau,Liste[i][0].y,Liste[i][0].x)
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
    while len(L)!=0 and increment<150000:
        increment += 1
        rate=True
        while s<2 and rate:

            while t<4 and rate:
                while j<=len(Plateau[0])-len(L[0].s[0]) and rate:
                    while i<=len(Plateau)-len(L[0].s) and rate: #colonne
                        nP=ajout(L[0],Plateau,i,j)
                        
                        if type(nP)!=str:
                            Plateau=nP
                            rate=False
                            Listedesdetails.append([L[0],t,s])  #[piece,tourne,symetrie,ligne, colonne]
                        print(Listedesdetails,j)
                        i+=1
                    i=0

                    j+=1
                j=0

                L[0] = tourne90(L[0])
                t+=1
            t=0
            L[0][0].s = retourne(L[0][0])
            s+=1
        s=0
        if rate: #si la piece n'est pas posée
                        
            # print('Affichage de la liste des details (avant et après) \n',Listedesdetails) 
            #[piece,tourne,symetrie,ligne, colonne]
            if len(Listedesdetails)==0:
                return Plateau
            s,t,j,i=Listedesdetails[-1][2],Listedesdetails[-1][1],Listedesdetails[-1].x,Listedesdetails[-1].y
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
LP7=[BizarrdZ,IBarre2,PetitL,PetitV,Carre,Carre,PetitV,NormalP,PetitEclair,PetitV]
print("Katamino bon :\n", bourrin(LP7))