import matplotlib.pyplot as plt
import numpy as np

file = open("/home/apauper/Documents/MPSI1/Informatique/TIPE Esther Andreas/tipe-esther-andreas/resultats/nœuds.txt", 'r')
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
        if L[i][0]=='N':
            n=int(L[i-1])
            nœuds=int(L[i][16:])
            l.append((n,nœuds))
    return l

n_solu=f_to_list(file)

file.close()

#%% traitement
dico_taille={}
for elt in n_solu:
    n=elt[0]
    if n not in dico_taille:
        dico_taille[n]=[elt[1]]
    else:
        dico_taille[n].append(elt[1])
def liste_n(l):
    s=[]
    n=len(l)
    for i in range(n):
        s.append(l[i][0])
    return s
del dico_taille[0]
l_n=[]
m_n=[]

for taille in dico_taille:
    l_n.append(taille)
    m_n.append(np.mean(dico_taille[taille]))


#%% affichage
plt.figure(dpi=200)
plt.plot(l_n,m_n, '+')
plt.xlabel("Taille de la liste")
plt.ylabel("Nombre moyen de nœuds")
plt.yscale('log')


#%%
a,b=np.polyfit(l_n, np.log(m_n), 1)
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