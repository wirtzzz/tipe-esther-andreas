#RESOLUTION PAR BACKTRACKING
#%%definitions
from copy import *
from variables import *
Long=int(input("Long: "))
Large=int(input("large: "))
#Plateau=[[ False for i in range (Large)] for _ in range (Long)]


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
#format d'une pièceLP7
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
    elif len(Liste)==0: #s'il n'y a plus de kataminos à poser et que la grille n'est pas complète
        return 'pas une solution'
    elif len(Liste)==1 and N==Liste[0].area:
        CP=Coups_Possibles(Liste[0], Plateau, N)
        if len(CP)==0:
            return 'pas une solution'
        else:
            return [CP[0]]
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
                        solutions.append(newSolution[i]) #on ajoute les solutions trouvées
            return solutions

LP3bis=[NormalP,GrandEclair,NormalC]
LP5=[NormalP,IBarre3,PetitL,PetitT,IBarre4]
LPprob=[IBarre2,IBarre2,IBarre3,Carre,PetitT]
LP7=[BizarrdZ,PetitL,PetitV,Carre,Carre,PetitV,NormalP,PetitEclair,PetitV]
LP4=[GrandL,PetitT,GrandT,Carre,BizarrdZ,PetitEclair,IBarre3]


L6_0=[IBarre2,IBarre2,IBarre2,IBarre2,IBarre2,NormalP]  #5*3
L6_1=6*[NormalP]
A=Solution(LP7)

print(A)    #le dernier élément de chaque solution affiche la grille complétée
print(len(A))       #nombre de solutions trouvées
print(i)            #nombre d'essais
