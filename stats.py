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
for taille in dico_taille:
    l_n.append(taille)
    liste_nsol=liste_n(dico_taille[taille])
    m=np.mean(liste_nsol)
    e=np.std(liste_nsol)
    stats[0].append(m)
    stats[1].append(e)
    stats[2].append(len(liste_nsol))

#%% affichage
plt.figure(dpi=200)
plt.plot(l_n,stats[0])
plt.xlabel("Taille de la liste")
plt.ylabel("Nombre moyen de solutions")
plt.yscale('log')

#%% retirer les 0
def remove_zeros(L):
    l=[]
    for elt in L:
        if not elt==0:
            l.append(elt)
    return l

dico_taille2={}
for c in dico_taille:
    dico_taille2[c]=remove_zeros(dico_taille[c])
l_n=[]
stats2=[]
for taille in dico_taille2:
    l_n.append(taille)
    liste_nsol=liste_n(dico_taille2[taille])
    m=np.mean(liste_nsol)
    e=np.std(liste_nsol)
    stats2.append(m)

plt.figure(dpi=200)
plt.plot(l_n, stats2,'+')
plt.plot(l_n,stats2)
plt.xlabel("Taille de la liste")
plt.ylabel("Nombre moyen de solutions")
plt.yscale('log')