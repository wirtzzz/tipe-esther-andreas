#RESOLUTION PAR BACKTRACKING
#%%definitions
from copy import *
Long=int(input("Long: "))
Large=int(input("large: "))
#Plateau=[[ False for i in range (Large)] for _ in range (Long)]

#LISTE DES PIECES
class Katamino:
    def __init__(self, shape, p, sym, max_rot, x_coord=0, y_coord=0): 
        self.s=shape   #matrice représentant le katamino
        self.x=x_coord #stocke la coordonnée x du point (0,0) du katamino dans le tableau
        self.y=y_coord #coordonnée y
        self.priority=p
        self.symmetry=sym #booléen vrai si le katamino vérifie une symétrie axiale 
        self.max_r= max_rot #nombre de rotations par lesquels le katamino n'est pas invariant
        self.area=a    #aire du katamino

GrandL=Katamino([[4,4],[4,0],[4,0],[4,0]],4, False, 4,5)
GrandT=Katamino([[5,0],[5,5],[5,0],[5,0]],5, False, 4,5)
GrandEclair=Katamino([[3,0],[3,0],[3,3],[0,3]],3, False, 4)
GrandV=Katamino([[2,2,2],[2,0,0],[2,0,0]],2, False, 4)
NormalP=Katamino([[6,6],[6,6],[6,0]],6, False, 4)
NormalC=Katamino([[7,7],[7,0],[7,7]],7, True,4)
BizarrdZ=Katamino([[1,0,0],[1,1,1],[0,0,1]],1, False, 2)
IBarre4=Katamino([[8],[8],[8],[8]],8, True, 2)
PetitL=Katamino([[9,9],[9,0],[9,0]],9, False, 4)
PetitT=Katamino([[10,0],[10,10],[10,0]],10, True, 4)
PetitEclair=Katamino([[12,0],[12,12],[0,12]],12,False,2)
Carre=Katamino([[11,11],[11,11]],11,True,1)
IBarre3=Katamino([[13],[13],[13]],13, True,2)
PetitV=Katamino([[14,14],[14,0]],14,False,4)
IBarre2=Katamino([[15],[15]],15,True,2)
Point=Katamino([[16]], 16,True,1)

#%%opérations sur les kataminos
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
    NPiece=[ [0 for i in range (len(p[0]))] for _ in range (len(p))]
    for i in range (len(p)):
        for j in range (len(p[0])):
            NPiece[i][j]=p[i][len(p[0])-j-1]
    return NPiece
#AJOUT D'UNE PIECE AU PLATEAU
def ajout(Piece,Plateau=[[0 for _ in range(Large)] for _ in range (Long)],n=0,m=0):
    Nplateau=deepcopy(Plateau)
    for i in range (len(Piece.s)): #colonnes
        for j in range (len(Piece.s[0])): #lignes
            if Piece.s[i][j]:
                if i+n<len(Nplateau) and j+m< len(Nplateau[0]) and Nplateau[i+n][j+m]==0: #(andreas) petite modification pour vérifier que la pièce rentre bien
                    Nplateau[i+n][j+m]=Piece.s[i][j]  #faire un nouveau plateau
                else:
                    return "Erreur"
    return Nplateau
#format d'une pièce
def Aire(Katamino):
    A=0
    for i in range(len(Katamino.s)):
        for j in range(len(Katamino.s[0])):
            if Katamino.s[i][j] != 0:
                A+=1
    return A
def Aire_Liste(Liste):
    "renvoie la somme des aires des kataminos d'une liste"
    A_tot=0
    for K in Liste:
        A_tot+=K.area
    return A_tot
i=0

#%% backtracking
def Coups_Possibles(Kata,Plateau,n):
    """renvoie l'ensemble des coups possibles à partir d'une position donnée, Plateau, avec une pièce Kata
    n est l'aire libre du plateau"""
    i=0
    K=deepcopy(Kata)    #on copie le katamino
    K.x,K.y,r=0,0,0 #on initialise la position du katamino à (0,0) et le nombre de rotations à 0
    Coups=[] #liste des coups possibles à partir de la position
    smax= 0 #initialisation du nombre de "retournements" de la pièce
    s=0 
    if n-K.area<0:  #s'il n'y a plus de place sur le plateau
        return "pas de coups possibles à partir de cette position"
    if not K.symmetry:  #si la pièce n'admet pas de symétrie axiale il faudra la retourner
        smax+=1
    while s<=smax:
        while r<K.max_r:
            while K.x <= (len(Plateau)-len(K.s)):
                while K.y <= (len(Plateau[0])-len(K.s[0])):
                    NP=ajout(K,Plateau,K.x,K.y)          #on ajout K au plateau dans NP, variable temporaire
                    i+=1
                    if type(NP) != str: #si le coup est possible
                        Coups.append(NP)
                    K.y+=1
                K.y=0
                K.x+=1
            K.x=0
            K.s=tourne90(K)
            r+=1
        r=0
        K.s=retourne(K)
        s+=1
    if len(Coups)==0:
        return "pas de coups possibles à partir de cette position"
    else:
        return (Coups,n-K.area)

def Solution(Liste, Plateau=[[0 for _ in range(Large)] for _ in range (Long)],N=Long*Large):
    """renvoie toutes les solutions possibles d'un problème
    Liste est une liste de Kataminos, Plateau une matrice et N un entier"""
    if len(Liste)==0 and N==0: #vérifie que plateau est rempli
        return [[]]
    elif len(Liste)==0: #s'il n'y a plus de kataminos à poser et que la grille n'est pas compléte
        return 'pas une solution'
    else:
        CP=Coups_Possibles(Liste[0], Plateau, N)
        if type(CP)==str:
            return 'pas une solution'
        else:
            solutions=[]
            Coups,n=CP
            for coup in Coups:
                newSolution=Solution(Liste[1:],coup,n)  #en partant de chaque coup on cherche les solutions possibles
                for i in range(len(newSolution)):
                    if type(newSolution[i]) != str:
                        solutions.append([coup]+newSolution[i]) #on ajoute les solutions trouvées
            return solutions
    
LP3bis=[NormalP,GrandEclair,NormalC]
LP5=[NormalP,IBarre3,PetitL,PetitT,IBarre4]
LPprob=[IBarre2,IBarre2,IBarre3,Carre,PetitT]
LP7=[BizarrdZ,PetitL,PetitV,Carre,Carre,PetitV,NormalP,PetitEclair,PetitV]
LP4=[GrandL,PetitT,GrandT,Carre,BizarrdZ,PetitEclair,IBarre3]

A=Solution(LP5)

for s in A:
    print(s[-1])    #le dernier élément de chaque solution affiche la grille complétée
print(len(A))       #nombre de solutions trouvées
print(i)            #nombre d'essais