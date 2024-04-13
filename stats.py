import matplotlib.pyplot as plt
import numpy as np

file = open("/home/apauper/Documents/MPSI1/Informatique/TIPE Esther Andreas/tipe-esther-andreas/resultats.txt", 'r')
n_solu=[]

def str_to_list(s):
    n=len(s)
    L=[]
    for i in range(n):
        if 65<=ord(s[i]) and ord(s[i])<=90:
            L.append(s[i]+s[i+1])
    return L

def f_to_list(f):
    L=file.readlines()
    l=[]  
    for i in range(len(L)):
        if L[i][0]=='[':
            n=L[i+1][20:-1]
            l.append((int(n),str_to_list(L[i])))
    return l

n_solu=f_to_list(file)

file.close()

#%% traitement
dico_taille={}
for elt in n_solu:
    n=len(elt[1])
    if n not in dico_taille:
        dico_taille[n]=[elt]
    else:
        dico_taille[n].append(elt)
def liste_n(l):
    s=[]
    n=len(l)
    for i in range(n):
        s.append(l[i][0])
    return s

l_n=[]

stats=[[],[],[]]
for c in dico_taille:
    l_n.append(c)
    liste_nsol=liste_n(dico_taille[c])
    m=np.mean(liste_nsol)
    e=np.std(liste_nsol)
    stats[0].append(m)
    stats[1].append(e)
    stats[2].append(len(liste_nsol))
plt.plot(l_n,np.log(stats[0]))