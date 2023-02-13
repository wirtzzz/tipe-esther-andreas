from tkinter import *
import copy
#à partir d'ici c'est la merde
#%% lesdits kataminos

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
Grid=[[0 for _ in range(13)] for _ in range(5)]
def RotateKataClockwise(Kata):          #tourner la pièce dans le sens horaire, fonctionne
    newKata=[]
    for i in range(len(Kata[0])):
        kataL=[]
        for j in range(len(Kata)):
            kataL.append(Kata[len(Kata)-j-1][i])
        newKata.append(kataL)
    return newKata

def FlipKata(Kata):                     #retourner la pièce
    newKata=[]
    for i in range(len(Kata)):
        kataL=[]
        for j in range(len(Kata[0])):
            kataL.append(Kata[i][len(Kata[0])-j-1])
        newKata.append(kataL)
    return newKata

def FitKataInGrid(Kata,G,flip):              #fonction qui cherche à faire rentrer un kata dans une grille donnée (elle marche promis)
    newG=copy.deepcopy(G)
    newKata=copy.deepcopy(Kata)
    for _ in range(4):
        u,v=0,0
        while u+len(newKata)<=len(newG):
            while v+len(newKata[0])<=len(newG[0]):
                newG=copy.deepcopy(G)
                fitting=True
                for i in range(len(newKata)):
                    for j in range(len(Kata[0])):
                        if newG[i+u][j+v]==0 or newKata[i][j]==0:               #ajoute le morceau de Kata dans le cas où la case est vide
                            newG[i+u][j+v]+=newKata[i][j]
                            print(newG)
                        else:
                           fitting=False
                if fitting:
                    return newG
                v+=1
            u+=1
            v=0
        newKata=RotateKataClockwise(newKata)
    if flip:    
        return FitKataInGrid(FlipKata(Kata), G, False)
    return G

#%% résoudre le katamino
KataL=[GrandEclair,GrandL,GrandT]
def TestCombination(KataList, G):
    