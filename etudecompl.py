
import numpy as np
import matplotlib.pyplot as plt
from os import chdir

chdir('C:/Users/esthe/Desktop/TIPE')

Liste15=open('combi/L15.txt','r')

Listes=Liste15.readlines()

Liste15.close()

compl=0

LONG=3 #int(input("Longueur du plateau : "))
LARGE=5 #int(input("Largeur du plateau : "))

Plateau=[[0 for _ in range (LARGE)] for _ in range (LONG)]


def tri_insertion (L):
    n=len(L)
    for i in range (1,n):
        j=i
        x=L[i]
        
        while 0<j and x<L[j-1]:
            L[j]=L[j-1]
            j=j-1
        L[j]=x
        
def lenvers(L):
    n=len(L)
    for i in range (n//2):
        L[i],L[n-i-1]=L[n-i-1],L[i]

#LISTE DES PIECES
GrandL=[[1,1],[1,0],[1,0],[1,0]]
GrandT=[[2,0],[2,2],[2,0],[2,0]]
GrandEclair=[[3,0],[3,0],[3,3],[0,3]]
GrandV=[[4,4,4],[4,0,0],[4,0,0]]

NormalP=[[5,5],[5,5],[5,0]]
NormalC=[[6,6],[6,0],[6,6]]
BizarrdZ=[[7,0,0],[7,7,7],[0,0,7]]
#NormalZ=[[7,0,0],[7,7,7],[0,0,7]]

PetitL=[[8,8],[8,0],[8,0]]
PetitT=[[9,0],[9,9],[9,0]]
PetitV=[[10,10],[10,0]]
PetitEclair=[[11,0],[11,11],[0,11]]

#Barre4=[[12],[12],[12],[12]]
#Barre3=[[13],[13],[13]]
#Barre2=[[14],[14]]
IBarre4=[[12],[12],[12],[12]]
IBarre3=[[13],[13],[13]]
IBarre2=[[14],[14]]

Carre=[[15,15],[15,15]]
Point=[[16]]


#pas de jugements plz
for i in range(len(Listes)):
    Listes[i]=Listes[i][1:len(Listes[i])-2].split(',')
    
def f(L):
    for i in range (len(L)):
        for j in range (len(L[i])):
            if L[i][j][0]=='G':
                if L[i][j][-1]=='L':
                    L[i][j]=GrandL
                if L[i][j][-1]=='T':
                    L[i][j]=GrandT
                if L[i][j][-1]=='r':
                    L[i][j]=GrandEclair
                if L[i][j][-1]=='V':
                    L[i][j]=GrandV
                
            elif L[i][j][0]=='N':
                if L[i][j][-1]=='P':
                    L[i][j]=NormalP
                if L[i][j][-1]=='C':
                    L[i][j]=NormalC
                
            elif L[i][j][0]=='P':
                if L[i][j][-1]=='L':
                    L[i][j]=PetitL
                if L[i][j][-1]=='T':
                    L[i][j]=PetitT
                if L[i][j][-1]=='V':
                    L[i][j]=PetitV
                if L[i][j][-1]=='r':
                    L[i][j]=PetitEclair
                if L[i][j][-1]=='t':
                    L[i][j]=Point
                
            elif L[i][j][0]=='I':
                
                if L[i][j][-1]=='2':
                    L[i][j]=IBarre2
                if L[i][j][-1]=='3':
                    L[i][j]=IBarre3
                if L[i][j][-1]=='4':
                    L[i][j]=IBarre4
                    
            elif L[i][j][0]=='C':
                L[i][j]=Carre  
                
            else:
                L[i][j]=BizarrdZ            



f(Listes)




#ROTATION D'UNE PIECE DE 90°
def tourne90(Piece): 
    "tourne une pièce de 90° dans le sens horaire"
    "Piece est une matrice"
    global compl
    NPiece=[ [0 for _ in range (len(Piece))] for _ in range (len(Piece[0]))] #on crée une matrice vide
    for i in range (len(Piece)): #lignes
        for j in range (len(Piece[0])): #colonnes
            NPiece[j][i]=Piece[len(Piece)-1-i][j] #on fait la transposée et la symétrie par rapport à l'axe des ordonnées
            compl+=2
    Piece=NPiece
    return Piece

#SYMETRIE par l'ordonnée
def retourne(Piece):
    "effectue la symétrie une pièce par l'ordonnée en place"
    "Piece est une matrice"
    global compl
    NPiece=[ [0 for i in range (len(Piece[0]))] for _ in range (len(Piece))]
    for i in range (len(Piece)):
        for j in range (len(Piece[0])):
            NPiece[i][j]=Piece[i][len(Piece[0])-j-1]
            compl+=2
    return NPiece

#AJOUT D'UNE PIECE AU PLATEAU
def ajout(Piece, Plateau=[[0 for _ in range(LARGE)] for _ in range (LONG)], l=0, c=0): 
    "ajoute une pièce à un plateau"
    "Piece et Plateau sont des matrices, Plateau est par défaut une matrice nulle, l et c int par défaut 0"
    global compl
    # (l,c) correspond aux coordonnées de la case (0,0) de la piece dans le plateau
    Nplateau=np.copy(Plateau) #on fait un nouveau plateau 
    for i in range (len(Piece)): #lignes
        for j in range (len(Piece[0])): #colonnes
            if Piece[i][j]!=0: 
                if Nplateau[i+l][j+c]==0: #si la case du plateau est vide
                    Nplateau[i+l][j+c]=Piece[i][j] #on pose la case de piece
                    compl+=4
                else:
                    compl+=2
                    return False #sinon la pièce ne peut pas être posée
    return Nplateau #on retourne le nouveau plateau

#APPLIQUE UNE LISTE DE PIECES A UN PLATEAU
def applique(Liste, Plateau=[[0 for _ in range(LARGE)] for _ in range (LONG)]):
    "applique la liste de pièces à un plateau par défaut une matrice nulle"
    "Liste contient une liste de [piece,tourne,symetrie,ligne,colonne]"
    global compl
    for i in range (len(Liste)):
        Plateau = ajout(Liste[i][0], Plateau, Liste[i][3], Liste[i][4]) 
    return Plateau
    
    
#print(applique(Liste=[[GrandL,0,0,0,3],[Barre4,0,0,1,4],[Barre3,0,0,0,0],[Carre,0,0,0,1],[tourne90(PetitEclair),0,1,2,0],[tourne90(retourne(GrandT)),1,1,3,0]] #[piece,tourne,symetrie,ligne, colonne]
def force_brute(Liste, Plateau=[[0 for _ in range(LARGE)] for _ in range (LONG)]):
    "résoud un Katamino avec les pièces données dans la liste"
    "teste toutes les possibilitées avant d'en trouver une qui fonctionne"
    global compl
    L=np.copy(Liste) #liste des pieces de départ
    Lparams=[] #contient [piece,tourne,symetrie,ligne,colonne]
    s,t,i,j=0,0,0,0 #compteurs de symetrie, tourne, ligne et colonne
    k = 0 #compteur de tours
    while len(L)!=0 and k<15000:
        k += 1
        posee=False #au départ la piece n'est pas posée
        
        #on teste toutes les possibilités de positionnement de la piece
        while s<2 and not posee: #symetrie
            compl+=1
            while t<4 and not posee: #tourne
                compl+=1
                while i<=len(Plateau)-len(L[0]) and not posee: #ligne
                    compl+=2
                    while j<=len(Plateau[0])-len(L[0][0]) and not posee: #colonne
                        compl+=2
                        nP = ajout(L[0],Plateau,i,j)
                        if type(nP)!=bool :
                            Plateau = nP
                            posee=True
                            Lparams.append([L[0],s,t,i,j])  #[piece,tourne,symetrie,ligne, colonne]
                        j+=1
                    j=0
                    i+=1
                i=0
                L[0]=tourne90(L[0])
                t+=1
            t=0
            L[0]=retourne(L[0])
            s+=1
        s=0
        if not posee: #si la piece n'est pas posée
            if len(Lparams)==0:
                return Plateau, "échec"
            
            L=Liste[len(Liste)-len(L)-1:] #on ajoute la pièce d'avant aux pieces non posées
            compl+=2
            L[0], s, t, i, j =Lparams[-1][0], Lparams[-1][1], Lparams[-1][2], Lparams[-1][3], Lparams[-1][4] #pour reprendre la on on s'était arreté avec la pièce davant
            Lparams=Lparams[:-1] #on retire la pièce d'avant des pieces posées
            
            if i>len(Plateau)-len(L[0]): 
                i=0
                if j>len(Plateau[0])-len(L[0][0]): 
                    j=0
                    if t>3:
                        t=0
                        if s>0:
                            #Toutes les positions ont été testées ...
                            ()
                        else:
                            s+=1
                            L[0]=retourne(L[0])
                            compl+=3
                    else:
                        t+=1
                        L[0]=tourne90(L[0])
                        compl+=3
                else:
                    j+=1
                    compl+=3
            else: 
                i+=1
                compl+=2
            Plateau=applique(Lparams) #on reprend le plateau sans la pièce d'avant
            
        else:
            L=L[1:] # liste des pieces restantes

        #print('\nAffichage du plateau', k,' \n',Plateau)
    return Plateau

#TESTS
LP3=[NormalC,GrandEclair,NormalP]
LP3bis=[NormalP,GrandEclair,NormalC]
LP4=[GrandL,PetitT,GrandT,Carre,BizarrdZ,PetitEclair,IBarre3]
LP5=[NormalP,IBarre3,PetitL,PetitT,IBarre4]#4,5 fonctionne mais pas 5,4 
LP6=[GrandT,GrandL,PetitL,GrandV,Carre,IBarre2]
#Liste=[[GrandL,0,0,0,3],[Barre4,0,0,1,4],[Barre3,0,0,0,0],[Carre,0,0,0,1],[PetitEclair,0,1,2,0],[GrandT,1,1,3,0]] #[piece,tourne,symetrie,ligne, colonne]
LP7=[NormalP,GrandL,BizarrdZ,GrandEclair,IBarre4,Point]
#print("Katamino en force brute :\n", force_brute(LP5))

#LL=PermutationsListe(LP4)

#Lpiece1=[]

#for i in range (len(LL)):
#    compl=0
#    force_brute(LL[i])
#    Cs.append([compl])
#    Lpiece1.append(LL[i][0][0][0])
#    print (LL[i][0],'\n',compl,'\n',i,'/',5040)


truc=["liste des listes qui font 5*k"]
Cs2=[]
Cs1=[]
#•622, 608,506,43,60qqchose
#◘ajouter l'autre plateau
for i in range (624,len(Listes)):
    compl=0
    tri_insertion(Listes[i])
    force_brute(Listes[i])
    compl1=compl
    
    compl=0
    lenvers(Listes[i])
    force_brute(Listes[i])
    #Lpiece1.append(LL[i][0])
    compl2=compl
    
    Cs2.append(compl2)
    Cs1.append(compl1)
    print ('coucou\n',compl,'\n',i,'/','beaucoup')
    
    
plt.plot(Cs1,Cs2,'*')
plt.show
