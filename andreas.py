from tkinter import *
import copy
#à partir d'ici c'est la merde
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

#%% tourner le kata
Grid=[[0 for _ in range(13)] for _ in range(5)]
Kata1=[[1,1,1],[0,1,0],[1,1,0]]
Kata2=[[0,2],[0,2],[2,2]]
def RotateKataClockwise(Kata):          #tourner la pièce dans le sens horaire, fonctionne
    newKata=[]
    for i in range(len(Kata[0])):
        kataL=[]
        for j in range(len(Kata)):
            kataL.append(Kata[len(Kata)-j-1][i])
        newKata.append(kataL)
    return newKata

def FitKataInGrid(Kata,G):              #fonction qui cherche à faire rentrer un kata dans une grille donnée
    newG=copy.deepcopy(G)
    for _ in range(4):
        u,v=0,0
        newKata=copy.deepcopy(Kata)
        while u+len(newKata)<=len(newG):
            while v+len(newKata[0]):
                newG=copy.deepcopy(G)
                fitting=True
                for i in range(len(newKata)):
                    for j in range(len(Kata[0])):
                        if newG[i+u][j+v]==0 or newKata[i][j]==0:               #ajoute le morceau de Kata dans le cas où la case est vide
                            newG[i+u][j+v]+=newKata[i][j]
                        else:
                           fitting=False
                if fitting:
                    return newG
                v+=1
            u+=1
        newKata=RotateKataClockwise(newKata)
