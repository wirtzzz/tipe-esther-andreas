from tkinter import *

#à partir d'ici c'est la merde
#%% maths et dessin
def DrawKatamino(Kata, pos, col):
    u,v = pos
    for i in range(len(Kata)):
        for j in range(len(Kata[i])):
            print(i*100," ",j*100)
            
            if Kata[i][j]==1:
                canvas.create_rectangle(v+j*100, u+i*100, v+(j+1)*100,u+(i+1)*100,
                                    outline=col,
                                    fill=col)

def DrawGrid(Grid):
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
 
L=[[0,1],[0,1],[1,1]]
#DrawKatamino(L, (200 ,300), "#0ff")
DrawGrid([[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]])
canvas.pack()

ws.mainloop()

#%% tourner le kata
Grid=[[0 for _ in range(13)] for _ in range(5)]
Kata1=[[1,1,1],[0,1,0],[1,1,0]]

def RotateKataClockwise(Kata):
    newKata=[]
    for i in range(len(Kata[0])):
        kataL=[]
        for j in range(len(Kata)):
            kataL.append(Kata[len(Kata)-j-1][i])
        newKata.append(kataL)
    return newKata

Kata2= RotateKataClockwise(Kata1)

