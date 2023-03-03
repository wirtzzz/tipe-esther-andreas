from tkinter import *
import copy
#%% lesdits kataminos
class Katamino:
    """peut etre pas si utile que ça mais pourquoi pas"""
    def __init__(self, shape, number, x_coord=0, y_coord=0, rotation=0, symetrie=0):
        self.s=shape
        self.n=number
        self.x=x_coord
        self.y=y_coord
        self.r=rotation
        self.ss=simetrie

GrandL=Katamino([[1,1],[1,0],[1,0],[1,0]],1)
GrandT=Katamino([[2,0],[2,2],[2,0],[2,0]],2)
GrandEclair=Katamino([[3,0],[3,0],[3,3],[0,3]],3)

GrandV=Katamino([[4,4,4],[4,0,0],[4,0,0]],4)

NormalP=Katamino([[5,5],[5,5],[5,0]],5)
NormalC=Katamino([[6,6],[6,0],[6,6]],6)

BizarrdZ=Katamino([[7,0,0],[7,7,7],[0,0,7]],7)

IBarre4=Katamino([[8],[8],[8],[8]],8)

PetitL=Katamino([[9,9],[9,0],[9,0]],9)
PetitT=Katamino([[10,0],[10,10],[10,0]],10)
PetitEclair=Katamino([[11,0],[11,11],[0,11]],11)

Carre=Katamino([[12,12],[12,12]],12)

IBarre3=Katamino([[13],[13],[13]],13)
PetitV=Katamino([[14,14],[14,0]],14)

IBarre2=Katamino([[15],[15]],15)

Point=Katamino([[16]], 16)


#%% maths et dessin
def DrawGrid(Grid):             #afficher la grille complétée
    col={1:"#00f",2:"#0f0",3:"#f00",4:"#dd0",5:"#0ff",6:"#f0f",7:"#800",8:"#080",9:"#008",10:"#880",11:"#808",12:"#888",13:"#400",14:"#040",15:"#004",16:"#044"}
    for i in range(len(Grid)):
        for j in range(len(Grid[i])):
            canvas.create_rectangle(j*100, i*100,(j+1)*100,(i+1)*100,
                                outline=col[Grid[i][j]],
                                fill=col[Grid[i][j]])
ws = Tk()
ws.title('TIPE')
ws.geometry('1000x1000')
ws.config(bg='#000')

canvas = Canvas(
    ws,
    height=1000,
    width=1000,
    bg="#fff"
    )
canvas.pack()
ws.mainloop()

#%% faire rentrer le kata
Grid=[[0 for _ in range(3)] for _ in range(5)]
def RotateKataClockwise(Kata):          #tourner la pièce dans le sens horaire, fonctionne
    newKata=copy.deepcopy(Kata)
    newKata.s=[]
    for i in range(len(Kata.s[0])):
        kataL=[]
        for j in range(len(Kata.s)):
            kataL.append(Kata[len(Kata.s)-j-1][i])
        newKata.s.append(kataL)
    return newKata

def FlipKata(Kata):                     #retourner la pièce
    newKata=copy.deepcopy(Kata)
    newKata.s=[]
    for i in range(len(Kata.s)):
        kataL=[]
        for j in range(len(Kata.s[0])):
            kataL.append(Kata[i][len(Kata[0])-j-1])
        newKata.s.append(kataL)
    return newKata

def FitKataInGrid(Kata,G,flip=True,init_rotation=0):
              #fonction qui cherche à faire rentrer un kata dans une grille donnée 
    newG=copy.deepcopy(G)
    newKata=copy.deepcopy(Kata)
    for _ in range(init_rotation):
        newKata=RotateKataClockwise(newKata)
    for _ in range(4):
        u,v=0,0
        while u+len(newKata.s)<=len(newG):
            while v+len(newKata.s[0])<=len(newG[0]):
                newG=copy.deepcopy(G)
                fitting=True
                for i in range(len(newKata)):
                    for j in range(len(nawKata.s[0])):
                        if newG[i+u][j+v]==0 or newKata.s[i][j]==0:               #ajoute le morceau de Kata dans le cas où la case est vide
                            newG[i+u][j+v]+=newKata.s[i][j]
                        else:
                           fitting=False
                if fitting:
                    Kata.x,Kata.y=u,v
                    return newG
                v+=1
            u+=1
            v=0
        newKata=RotateKataClockwise(newKata)
    if flip:    
        return FitKataInGrid(FlipKata(newKata), G, False)
    return G

def RemoveKata(Grid,n):
    for i in range(len(Grid)):
        for j in range (len(Grid[0])):
            if Grid[i][j]==n:
                Grid[i][j]=0
#def MoveKata(KataN,)
#%% résoudre le katamino
#KataL=[copy.deepcopy(NormalC),copy.deepcopy(NormalP),copy.deepcopy(GrandT)]
#def PermutationsListe(L): #tester les permutations d'une liste qconque, peut être pas utile
#    if len(L)==2:
#        return [L, [L[1], L[0]]]
#    else:
#        combL=[]
#        for i in range(len(L)):
#            l=PermutationsListe(L[:i]+L[i+1:])
#            for j in range(len(l)):
#                combL.append(l[j]+[L[i]])
#        return combL

def SolveKatamino(L, G):
    "teste les permutations d'une liste donnée de kataminos dans une grille"
    fitting=True
    newG=copy.deepcopy(G)
    for k in range(4):
        newG=FitKataInGrid(L[0].s, newG, k)
        for i in range(1,len(L)):
            newG=FitKataInGrid(L[i].s, newG)
        i,j=0,0
        while i<len(newG):
            j=0
            while j<len(newG[0]):
                if newG[i][j]==0:
                    fitting = False
                j+=1
            i+=1
        if fitting:
            return newG
        while L[0].x<=len(newG)-len(L[0].s):
            while L[0].y<=len(newG)-len(L[0].y)
        
    return newG


