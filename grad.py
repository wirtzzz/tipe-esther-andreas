#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:03:14 2023

@author: apauper
"""
from PIL import Image
import numpy as np


img=Image.open('/home/apauper/Documents/Informatique/lycee.jpg')
M=np.array(img, np.uint8)
def rotation90(img):
    N=np.array(img,np.uint8)
    n,m=len(N),len(N[0])
    M= np.zeros((m,n,3), np.uint8)
    for i in range(n):
        for j in range(m):
            M[n-j-1][i][:]=N[i][j][:]
    return M
Image.fromarray(rotation90(img))
#%%
def agrandissement(img,f):
    N=np.array(img, np.uint8)
    n,m=len(N),len(N[0])
    M=np.zeros((f*n,f*m,3), np.uint8)
    for i in range(n):
        for j in range(m):
            for k in range(f):
                for l in range(f):
                    M[i*f+k][j*f+l]=N[i][j]
    return M
Image.fromarray(agrandissement(img, 10))
#%%
def reduction(img,f):
    N=np.array(img,np.uint8)
    n,m=len(N),len(N[0])
    M=np.zeros((n//f,m//f,3),np.uint8)
    for i in range(n//f):
        for j in range(m//f):
            M[i][j]=N[i*f][j*f]
            
    return M
Image.fromarray(reduction(img, 4))

#%%
img1=Image.open('/home/apauper/Documents/Informatique/Einstein.jpg')
def convolution(img,N):
    L=np.array(img)
    n,m=len(L),len(L[0])
    M=np.zeros((n,m),np.uint8)
    for i in range(1,n-1):
        for j in range(1,m-1):
            for k in range(3):
                for l in range(3):
                    M[i][j]=M[i][j]+L[i+l-1][j+k-1]*N[l-1][k-1]
    return M
N=np.array([[1,2,1],[2,4,2],[1,2,1]])/16
Image.fromarray((convolution(img, N))
#%% 
def convolution_c(img,N):
    L=np.array(img)
    n,m=len(L),len(L[0])
    M=np.zeros((n,m,3), np.uint8)
    for i in range(1,n-1):
        for j in range(1,n-1):
            for k in range(3):
                for l in range(3):
                    u,v,w=L[i+l-1][j+k-1]
                    x=N[l-1][k-1]
                    M[i][j]=M[i][j]=x*u+x*v+x*w
    return M
Image.fromarray(convolution_c(img, N))
#%%
def gradient(img):
    L=np.array(img)
    n,m=len(L),len(L[0])
    M=np.zeros((n,m),np.uint8)
    for i in range(1,n-1):
        for j in range(1,m-1):
            gx=L[i][j+1]-L[i][j-1]
            gy=L[i-1][j]-L[i+1][j]
            M[i][j]=int(np.sqrt(gx**2+gy**2))
    return M
Image.fromarray(gradient(img1))

L=gradient(img)

