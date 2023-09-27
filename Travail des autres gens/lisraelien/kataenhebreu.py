import copy       #מסייע בהמשך בהעתקת רשימות בתוך רשימות
import matplotlib.pyplot as plt           #רעיון מעניין להצגה גרפית של הפתרון

#כל צורה במשחק מקבלת שם ומטריצה

# אם נעמיד את תת הרשימות אחת מתחת לשנייה נוכל לראות את הצורה#



#shapes:
X=[[0,1,0],[1,1,1],[0,1,0]]
P=[[2,2,2],[0,2,2],[0,0,0]]
Z=[[3,3,0],[0,3,0],[0,3,3]]
F=[[0,0,0,0],[0,0,0,0],[0,4,0,0],[4,4,4,4]]
L=[[5,5,5,5],[0,0,0,5],[0,0,0,0],[0,0,0,0]]
V=[[6,0,0],[6,0,0],[6,6,6]]
R=[[0,7,7],[7,7,0],[0,7,0]]
T=[[0,8,0],[0,8,0],[8,8,8]]
H=[[9,9,0],[0,9,0],[9,9,0]]
W=[[0,0,10],[0,10,10],[10,10,0]]
N=[[0,11,11,11],[11,11,0,0],[0,0,0,0],[0,0,0,0]]
I=[[12,0,0,0],[12,0,0,0],[12,0,0,0],[12,0,0,0]] 
#כל פאזל מורכב מחלקים שונים וכאן אנו מזינים את החלקים בחידה הספציפית
#here you put the parts in the riddle:
katamino=[L,V,P,H,W,F]


#here we build the board


num_parts=len(katamino)
#creating the board
Board=[]
for i in range (num_parts):
    Board.append([0,0,0,0,0])
#here we rotate the shape including mirror image     כאן מסובים את הצורה כולל תמונת ראי 
def rotateMatrix(matx):
    N=len(matx[0])
    mat = copy.deepcopy(matx)
    # Consider all squares one by one
    for x in range(0, 2):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N - x - 1):
            # store current cell in temp variable
            temp = mat[x][y]

            # move values from right to top
            mat[x][y] = mat[y][N - 1 - x]

            # move values from bottom to right
            mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]

            # move values from left to bottom
            mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]

            # assign temp to left
            mat[N - 1 - y][x] = temp

    return mat

def allShapeForms(shape):
        s = []
        s.append(shape)
        cp = copy.deepcopy(shape)
        for i in range(3):
            x = rotateMatrix(cp)
            s.append(x)
            cp = x
        cp = []
        for item in shape:
            cp.append(item[::-1])
        s.append(cp)
        for i in range(3):
            x = rotateMatrix(cp)
            s.append(x)
            cp = x
        return s


#here we fit shape to board  כאן מתאימים צורה ללוח שלנו

#that the shape will not get out of the board שהצורה לא תצא מהלוח
def fitForm2Board (form,tempboard):
    board=copy.deepcopy(tempboard)
    combinationFormList=[]
    collision = 0
    for y in range(num_parts):
        for x in range (5):
            for index, row in enumerate(form):
                for ind, cell in enumerate(row):


                    if cell != 0:
                        if (index+y<num_parts and ind+x<5) and (board[index+y][ind+x] == 0):
                                board[index+y][ind+x] = cell
                        else:
                            collision += 1

            if collision > 0:
                collision = 0
                board = copy.deepcopy(tempboard)

            else:
                combinationFormList.append(board)
                board =copy.deepcopy(tempboard)

    return combinationFormList

#פונקציה קטנה להצגת  מטריצה בדו מימד במקום כרשימה אחת ארוכה
def print2d(mat):
    for item in mat:
        print(item)

#כאן בודקים היכן יש מקומות ריקים בלוח בשכנות לצורה שלנו
def emptyNeighbors(y,x,board):
    nbrs = []
    if board[y][x] == 0:
        if (y - 1) >= 0 and board[y - 1][x] == 0:
            nbrs.append((y - 1, x))
        if (y + 1) <= (num_parts - 1) and board[y + 1][x] == 0:
            nbrs.append((y + 1, x))
        if (x - 1) >= 0 and  board[y][x - 1] == 0:
            nbrs.append((y, x - 1))
        if (x + 1) <= 4 and board[y][x + 1] == 0:
            nbrs.append((y, x + 1))
    else:
        return None
    return nbrs
#כדי לצמצם אפשרויות אנו מסירים לוחות אם איים ריקים שאינם מתאימים לשום צורה
def chekSmallCloseTeritoriesInBoard (board):
    for y in range (num_parts):
        for x in range (5):
            if emptyNeighbors(y,x,board)!=None and len(emptyNeighbors(y,x,board))==0:
                    return False
            if emptyNeighbors(y,x,board)!=None and len(emptyNeighbors(y,x,board))==1:
                z=emptyNeighbors(y,x,board)[0][0]
                k=emptyNeighbors(y,x,board)[0][1]
                if len(emptyNeighbors(z,k,board))==1:
                    return False
            if emptyNeighbors(y,x,board)!=None and len(emptyNeighbors(y,x,board))==2:
                z=emptyNeighbors(y,x,board)[0][0]
                k=emptyNeighbors(y,x,board)[0][1]
                g=emptyNeighbors(y,x,board)[1][0]
                h=emptyNeighbors(y,x,board)[1][1]
                if len(emptyNeighbors(z,k,board))==1 and len(emptyNeighbors(g,h,board))==1 :
                    return False
    return True
#כאן אנו מייצרים את האפשרויות השונות של הלוחות לכל צורה וצורה
#return all bords:
def allShapePossibilities (shape,board):
    allposs=[]
    for item in allShapeForms(shape):
        for b1 in fitForm2Board(item, board):
            if chekSmallCloseTeritoriesInBoard(b1):
                allposs.append(b1)
    return allposs
#כאן כתובה הפונקציה הראשית שפותרת את החידה כלולאה מקוננת

#nested loop to solve the puzzle and find us the winnig board
Num = 0
def findAll (board):
    global Num
    for b in allShapePossibilities(katamino[Num],board):
        if Num==num_parts-1:
                    print2d(b)
                    z = board #for the graphics
                    for ind, row in enumerate(z):
                        for index, num in enumerate(row):
                            if num == 1:
                                z[ind][index] = 1
                            if num == 2:
                                z[ind][index] = 2
                            if num == 3:
                                z[ind][index] = 3
                            if num == 4:
                                z[ind][index] = 4
                            if num == 5:
                                z[ind][index] = 5
                            if num == 6:
                                z[ind][index] = 6
                            if num == 7:
                                z[ind][index] = 7
                            if num == 8:
                                z[ind][index] = 8
                            if num == 9:
                                z[ind][index] = 9
                            if num == 10:
                                z[ind][index] = 10
                            if num == 11:
                                z[ind][index] = 11
                            if num == 12:
                                z[ind][index] = 12
                    fig = plt.figure()
                    ax = fig.add_subplot(111)
                    ax.imshow(z, extent=[1, 5, 1, num_parts], interpolation='none')
                    plt.show()
                    quit()
        else:
            Num+=1
            findAll(b) #nested loop כאן הלוואה המקוננת המחזירה את עצמה עד שמוצאת פתרון
            Num-=1 # if we didn't find solution in that path למקרה שלא מצאנו פתרון חוזרים צעד לאחור
findAll(Board) #הפעלת הפונקציה הרקורסיבית המקוננת
