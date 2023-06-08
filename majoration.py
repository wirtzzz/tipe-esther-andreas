#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 20:24:44 2023

@author: apauper
"""
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
Plateau=[[0 for _ in range(3)] for _ in range(5)]
def countKataminoPos(Kata,Grid):
    n,m=len(Grid),len(Grid[0])
    i,j=len(Kata.s),len(Kata.s[0])
    if Kata.symmetric:
        s=1
    else:
        s=2
    if i>j:
        return (n-j+1)*(m-j+1)*s*Kata.max_r
    else:
        return (n-i+1)*(m-i+1)*s*Kata.max_r