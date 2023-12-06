# ======    le but est d'estimer le nombre de solutions par une résolution de systèmes linéaires
# En résolvant un système linéaire, on aura à la fin un certain nombre de paramètres qui permettent une estimation du nombre de solutions
# Étant donné que l'on a déjà un moyen de résoudre le problème initial il n'y a pas besoin de
# préciser à quoi les couples correspondent.

#objectif après linéarisation: afficher grilles
from copy import *
from variables import *

Large=int(input('large:'))
Long=int(input('long:'))

#on représente une équation linéaire par une liste de couples contenant à l'indice 0 le scalaire par lequel la variable à l'indice 1 est multiplié
#ex : [(x, GrandL), (y, GrandT), (z,NormalP)] qu'il faut égaler à 1,x=0 ou 1, y=0 ou 1, z=0 ou 1
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

#ajout théorique pour compléter la matrice
def ajout_th(Piece,M,k,l,Plateau=[[0 for _ in range(Large)] for _ in range(Long)],n=0,m=0):
    if len(Piece.s)+n<=len(Plateau) and len(Piece.s[0])+m<=len(Plateau[0]):
        for i in range(len(Piece.s)):
            for j in range(len(Piece.s[0])):
                if Piece.s[i][j]!=0:
                    M[i+n][j+m][1][(l,k)]=1
                    M[i+n][j+m][0]+=1
    return k+1


#format d'une pièceLP7
def Aire_Liste(Liste):
    "renvoie la somme des aires des kataminos d'une liste"
    A_tot=0
    for K in Liste:
        A_tot+=K.area
    return A_tot



#si ça marche: avantage : meilleure complexité que nouveau pour obtenir les solutions
def systeme_lin(Liste,Plateau=[[0 for _ in range(Large)] for _ in range(Long)]):
    M=[[[0,{}] for _ in range(Large)] for _ in range(Long)] #stocke le nb de variables enregistrées et le dico des variables
    L=Liste[:]
    l=0
    while L!=[]:
        s_max=0
        s,r=0,0
        L[0].x,L[0].y=0,0
        k=0
        if not L[0].symmetry:
            s_max=1
        while s<=s_max:
            while r<L[0].max_r:
                while L[0].x<=len(Plateau)+1:
                    while L[0].y<=len(Plateau[0])+1:
                        k=ajout_th(L[0], M, k,l, Plateau, L[0].x, L[0].y)
                        L[0].y+=1
                    L[0].y=0
                    L[0].x+=1
                L[0].x=0
                r+=1
            r=0
            s+=1
        L=L[1:]
        l+=1
    return M,len(Liste)

#on cherche ensuite à résoudre le système linéaire en considérant chaque liste comme une somme d'éléments de {0,1} qui doit égaler 1
def compatibilité(Liste,Plateau=[[0 for _ in range(Large)] for _ in range(Long)]):
    return Aire_Liste(Liste)==len(Plateau)*len(Plateau[0])

LP3bis=[NormalP,GrandEclair,NormalC]

def suppr_tous_dicos(M,val,e,d):
    u,v=e
    for i in range(len(M)):
        for j in range(len(M[0])):
            l=[]
            for elt in M[i][j][1].keys():
                a,b=elt
                if (e in M[i][j] and not elt==e) or (a==u and not b==v):
                    l.append(elt)
                    M[i][j][0]-=1
                    d[elt]=0
                    val
            for elt in l:
                del M[i][j][1][elt]

def suppr(p,dico1,dico2):
    """suppr p fois les éléments de dico1 dans dico2"""
    zeros=[]
    nouveau=0
    for elt in dico1[1]:
        if elt in dico2[1]:
            dico2[1][elt]-=dico1[1][elt]*p
        else:
            dico2[1][elt]=-p
            nouveau+=1
        if dico2[1][elt]==0:
            zeros.append(elt)
    for elt in zeros:
        del dico2[1][elt]
        dico2[0]-=1
    dico2[0]+=nouveau
#coeur du problème è_é
def pseudo_trigonaliser(sys,n):
    """trigonalise le système linéaire obtenu tant que possible"""
    k,l=len(sys),len(sys[0])
    val=[[1 for _ in range(l)] for _ in range(k)]   #enregistre la valeur de la somme de chaque ligne qui doit égaler 1
    for i in range(k):
        for j in range(l):      #pour chaque 'ligne' (ou case) on choisit un pivot et l'on cherche t
            if not sys[i][j][0] == 0:
                pivot=list(sys[i][j][1].keys())[0]
                p1=sys[i][j][1][pivot]
                for j1 in range(j+1,l):
                    if pivot in sys[i][j1][1]:
                        p=sys[i][j1][1][pivot]
                        suppr(p/p1,sys[i][j],sys[i][j1])
                        val[i][j1]-=val[i][j]*p/p1
                for i1 in range(i+1,k):
                    for j1 in range(l):
                        if pivot in sys[i1][j1][1]:
                            p=sys[i1][j1][1][pivot]
                            suppr(p/p1,sys[i][j],sys[i1][j1])
                            val[i1][j1]-=val[i][j]*p/p1


    return sys,val

def diviser(dico,p):
    for elt in dico[1]:
        dico[1][elt]/=p

def pseudo_diagonaliser(sys,val):
    """rendre le système diagonal tant que possible"""
    k,l=len(sys),len(sys[0])
    for i in range(k-1,-1,-1):
        for j in range(l-1,-1,-1):
            if not sys[i][j][0]==0:
                pivot=list(sys[i][j][1].keys())[0]
                p1=sys[i][j][1][pivot]
                diviser(sys[i][j],p1)
                val[i][j]/=p1
                for i1 in range(i):
                    for j1 in range(l):
                        if pivot in sys[i1][j1][1]:
                            p=sys[i1][j1][1][pivot]
                            suppr(p,sys[i][j],sys[i1][j1])
                            val[i1][j1]-=p/p1
                for j1 in range(j):
                    if pivot in sys[i][j1][1]:
                        p=sys[i][j1][1][pivot]
                        suppr(p,sys[i][j],sys[i][j1])
                        val[i][j1]-=p/p1
    return sys,val

#vérifier que la somme des a_ij pour pour j = 1

def count_sol(m):
    sol={}
    for i in range(len(m)):
        for j in range(len(m[0])):
            for a,b in m[i][j][1]:
                if a not in sol:
                    sol[a]={'l':1,(a,b):1}
                elif (a,b) not in sol[a]:
                    sol[a][a,b]=1
                    sol[a]['l']+=1
    p=1
    for key in sol:
        p*=sol[key]['l']
    return p

#def count_sol1(m,i,n):  #i indice du katamino, n nombre de kataminos
    

L=[IBarre2,IBarre2]