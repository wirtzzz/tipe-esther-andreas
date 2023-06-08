from copy import *

# kataminos


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

GrandL=Katamino([[4,4],[4,0],[4,0],[4,0]],4, False, 4)
GrandT=Katamino([[5,0],[5,5],[5,0],[5,0]],5, False, 4)
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

#on remplace les "true" par le nombre choisi pour le chiffre

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



def force_brute(Liste,Plateau=[[0 for _ in range(Large)] for _ in range (Long)]): #,n,m,t,s):
    
    Liste=[deepcopy(a) for a in Liste] #liste des pieces qui restent
    L=Liste[:]
    Listedesdetails=[]
    print(Plateau)
    input()
    if len(L)==0:
        return Plateau,increment
    s,t,i,j=0,0,0,0
    increment = 0
    while len(L)!=0 and increment<2000000:
        increment += 1
        i,j=L[0].x,L[0].y
        rate=True
        print(increment)
        while s<2 and rate:

            while t<L[0].max_r and rate:
                while j<=len(Plateau[0])-len(L[0].s[0]) and rate:
                    while i<=len(Plateau)-len(L[0].s) and rate: #colonne
                        nP=ajout(L[0],Plateau,i,j)
                        
                        print(i ,j )
                        print(L[0].s,nP)
                        if type(nP)!=str:
                            Plateau=nP
                            rate=False
                            
                            Listedesdetails.append([L[0],t,s])  #[piece,tourne,symetrie,ligne, colonne]
                            L[0].x,L[0].y=i,j
                            break
                        i+=1
                    i=0
                    j+=1
                j=0
                if rate:
                    L[0].s = tourne90(L[0])
                t+=1
            t=0
            if rate:
                L[0].s = retourne(L[0])
            s+=1
        s=0
        print("bip", L[0].s, L[0].x,L[0].y)
        if rate: #si la piece n'est pas posée
                        
            # print('Affichage de la liste des details (avant et après) \n',Listedesdetails) 
            #[piece,tourne,symetrie,ligne, colonne]
            if len(Listedesdetails)==0:
                print("l", [(a.x,a.y) for a in Liste])
                return Plateau,increment
            s,t,j,i=Listedesdetails[-1][2],Listedesdetails[-1][1],Listedesdetails[-1][0].x,Listedesdetails[-1][0].y
            L=Liste[len(Liste)-len(L)-1:]
            L[0]=Listedesdetails[-1][0]
            i,j=L[0].x,L[0].y
            if i>len(Plateau)-len(Listedesdetails[-1][0].s):#ptet un pb là
    
                i=0
                if j>len(Plateau[0])-len(Listedesdetails[-1][0].s[0]): #ptet un pb ici
                    j=0
                    if t>3:
                        t=0
                        if s==0:
                            s+=1
                    else:
                        t+=1
                else:
                    j+=1
            else: 
                i+=1
            L[0].x,L[0].y = i,j         
            print("oui", L[0].x, L[0].y)
            Listedesdetails=Listedesdetails[:-1]
            print(Plateau)
            nP=applique(Listedesdetails)
            if type(nP) != str:
                Plateau=nP
            print(Plateau)
        else:
            L=L[1:]
        print('\nAffichage du plateau', increment, ' \n')
        for l in Plateau:
            print(l)
    return (Plateau,increment)


LP2=[NormalP,retourne(GrandEclair),[[6, 0, 6], [6, 6, 6]]] #bon, là ça fonctionne mais jai triché
LP3=[NormalC,GrandEclair,NormalP]
LP3bis=[NormalP,GrandEclair,NormalC]
LP32=[BizarrdZ,GrandV,GrandEclair]
LP4=[GrandL,PetitT,GrandT,Carre,BizarrdZ,PetitEclair,IBarre3]
LP5=[NormalP,IBarre3,PetitL,PetitT,IBarre4]
LP7=[BizarrdZ,PetitL,PetitV,Carre,Carre,PetitV,NormalP,PetitEclair,PetitV]
LP9= [IBarre4,PetitL,NormalP,PetitV,NormalC,GrandL,IBarre2,PetitT,IBarre3]
print("Katamino bon :\n", force_brute(LP32))