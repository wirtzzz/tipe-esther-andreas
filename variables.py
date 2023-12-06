#LISTE DES PIECES
class Katamino:
    def __init__(self, shape, p, sym, max_rot, a, x_coord=0, y_coord=0): 
        self.s=shape   #matrice représentant le katamino
        self.x=x_coord #stocke la coordonnée x du point (0,0) du katamino dans le tableau
        self.y=y_coord #coordonnée y
        self.priority=p
        self.symmetry=sym #booléen vrai si le katamino vérifie une symétrie axiale 
        self.max_r= max_rot #nombre de rotations par lesquels le katamino n'est pas invariant
        self.area=a    #aire du katamino

GrandL=Katamino([[4,4],[4,0],[4,0],[4,0]],4, False, 4,5)
GrandT=Katamino([[5,0],[5,5],[5,0],[5,0]],5, False, 4,5)
GrandEclair=Katamino([[3,0],[3,0],[3,3],[0,3]],3, False, 4,5)
GrandV=Katamino([[2,2,2],[2,0,0],[2,0,0]],2, False, 4,5)
NormalP=Katamino([[6,6],[6,6],[6,0]],6, False, 4,5)
NormalC=Katamino([[7,7],[7,0],[7,7]],7, True,4,5)
BizarrdZ=Katamino([[1,0,0],[1,1,1],[0,0,1]],1, False, 2,5)
IBarre4=Katamino([[8],[8],[8],[8]],8, True, 2,4)
PetitL=Katamino([[9,9],[9,0],[9,0]],9, False, 4,4)
PetitT=Katamino([[10,0],[10,10],[10,0]],10, True, 4,4)
PetitEclair=Katamino([[12,0],[12,12],[0,12]],12,False,2,4)
Carre=Katamino([[11,11],[11,11]],11,True,1,4)
IBarre3=Katamino([[13],[13],[13]],13, True,2,3)
PetitV=Katamino([[14,14],[14,0]],14,False,4,3)
IBarre2=Katamino([[15],[15]],15,True,2,2)
Point=Katamino([[16]], 16,True,1,1)