#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:02:27 2023

@author: apauper
"""

img1=Image.open('/home/apauper/signal-2022-11-04-171608_002.jpeg')
import numpy as np
from PIL import Image

#%% ex1
def trace(A):
    if len(A)==len(A[0]):
        s=0
        for i in range (len(A)):
            s+=A[i][i]
        return s
    return "pas une matrice carrée"


def transposée(A):
    L=np.zeros((len(A[0]),len(A)),int)
    for i in range(len(A)):
        for j in range(len(A[0])):
            L[j][i]=A[i][j]
    return L

def produit(A,B):
    assert len(A[0])==len(B), "formats incompatibles"
    L=np.zeros((len(A),len(B[0])),int)
    for i in range(len(L)):
        for j in range(len(L[0])):
            for k in range(len(B)):
                L[i][j]+=A[i][k]*B[k][j]
    return L

#%% exercice 2
M=np.array([[255,0,127]], np.uint8)
img=Image.fromarray(M, mode="L")
img.show()

#%%
M=np.zeros((400,400), np.uint8)
s=0
for i in range(400):
    for j in range(400):
        if (i//50)%2==(j//50)%2:
            M[i][j]=255
img=Image.fromarray(M, mode="L")
img.show()

#%% exercice 3
M=np.array([[(255,0,0),(0,255,0),(0,0,255)],[(255,255,0),(0,255,255),(255,0,255)],[(255,255,255),(0,0,0),(127,127,127)]], np.uint8)
img=Image.fromarray(M, mode="RGB")
img.show()
#%%
M=np.zeros((400,600,3),np.uint8)
for i in range(400):
    for j in range(600):
        if j//200==0:
            M[i][j]=[0,0,255]
        elif j//200==1:
            M[i][j]=[255,255,255]
        else:
            M[i][j]=[255,0,0]
img=Image.fromarray(M,mode="RGB")
img.show()

#%%
M=M=np.zeros((400,600,3),np.uint8)

for i in range(400):
    for j in range(600):
        if int(np.sqrt((j-300)**2+(i-200)**2))<=120:
            M[i][j]=[255,0,0]
        else:
            M[i][j]=[255,255,255]
img=Image.fromarray(M, mode="RGB")
img.show()

#%% exercice 4
def inversion_couleurs(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j]=[255-A[i][j][0],255-A[i][j][1],255-A[i][j][2]]
    return A
img=Image.open('/home/apauper/Documents/Informatique/lycee.jpg')
M=np.array(img)
#inversion_couleurs(M)
#img=Image.fromarray(M,mode="RGB")
#img.show()
#%%
def niveaux_gris(img):
    for i in range(len(img)):
        for j in range(len(img[0])):
            img[i][j]=img[i][j][0]//3+img[i][j][1]//3+img[i][j][2]//3
    return img
M=niveaux_gris(M)
img=Image.fromarray(M,mode="RGB")
img.show()
#%%
def symetrie_verticale(img):
    for i in range(len(img)):
        for j in range(len(img[0])//2):
            a=np.copy(img[i][j])
            img[i][j]=np.copy(img[i][len(img[0])-j-1])
            img[i][len(img[0])-j-1]=np.copy(a)
    return img
#M=symetrie_verticale(M)
#img=Image.fromarray(M,mode="RGB")
#img.show()
def symetrie_horizontale(img):
    for i in range(len(img)//2):
        for j in range(len(img[0])):
            img[i][j],img[len(img)-i-1][j]=np.copy(img[len(img)-i-1][j]),np.copy(img[i][j])
    return img

def rotation90(img):
    L=np.zeros((len(img[0]),len(img),3),np.uint8)
    for i in range(len(L)):
        for j in range(len(L[0])):
            L[i][j]=img[len(img)-j-1][i]
    return img

M=rotation90(M)
img=Image.fromarray(M,mode="RGB")
img.show()

