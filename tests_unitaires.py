# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:41:41 2017

@author: piroulasau
"""



#Ce fichier contient les tests unitaires de toutes les fonctions crées dans le cadre du projet Labyrinthe


from random import*

############################################################################################################

def entree_infos_laby():
    """
    Fonction qui fait entrer par l'utilisateur les dimensions du labyrinthe
    Elle renvoie la hauteur et la largeur du labyrinthe
    """
    l=input("Entrez les dimensions du labyrinthe :\nLargeur :")
    h=input("Hauteur :")
    try:
        l=int(l)
        l=abs(l)
        h=int(h)
        h=abs(h)
    except:
        print("Merci d'entrer des dimensions qui sont des entiers.")
        entree_infos_laby()
    return (h,l)

print(entree_infos_laby())

############################################################################################################

def genere_matrice(h,l):
    """entree_infos_chemin
    Créé une matrice au bon format qui servira de base pour la création du labyrinthe
    """
    matrice=[[-1]*(2*l+1)]
    for i in range(h):
        liste=[-1]
        for j in range(l):
            liste.append(h*i+j)
            liste.append(-1)
        matrice.append(liste)
        matrice.append([-1]*(2*l+1))
    return matrice
    
print(genere_matrice(3,4))

############################################################################################################

def cases_adjacentes(h,l,case,cases):
    """
    Renvoie les connexions possibles d'une case donnée
    """
    i=[]
    d=[]
    if case-l>=0:
        d.append(case-l)
    if case%l!=0:
        d.append(case-1)
    if (case+1)%l!=0:
        d.append(case+1)
    if case+l<h*l:
        d.append(case+l)
    m=d[:]
    for k in m:
        if cases[case]==cases[k]:
            d.remove(k)
            i.append(k)
    return (d,i)
    
print(cases_adjacentes(5,5,19,[0, 0, 2, 2, 2, 5, 5, 2, 2, 2, 5, 5, 5, 2, 2, 15, 15, 17, 2, 2, 20, 15, 2, 2, 2]))

############################################################################################################

def genere_laby(h,l,matrice):
    """
    Génere un labyrinthe aléatoire à partir d'une matrice
    """
    cases=[i for i in range(h*l)]
    connect=[i for i in range(h*l)]
    fin=[0]*(h*l)
    while cases!=fin: #tant qu'au moins une case est isolée des autres
        r=connect[randint(0,len(connect)-1)]
        a=cases_adjacentes(h,l,r,cases)[0]
        if len(a)==0:
            connect.remove(r)
            continue
        if len(a)==1:
            connect.remove(r)
        m=a.pop(randint(0,len(a)-1))
        x=cases[m]
        y=cases[r]
        for i in range(len(cases)):
            if cases[i]==max(x,y):
                cases[i]=min(x,y)
                matrice[1+2*(i//l)][1+2*(i%l)]=min(x,y)
        matrice[1+m//l+r//l][m%l+r%l+1]=0
    return matrice
    
print(genere_laby(3,4,
                  [[-1, -1, -1, -1, -1, -1, -1, -1, -1], 
                   [-1, 0, -1, 1, -1, 2, -1, 3, -1], 
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1], 
                    [-1, 3, -1, 4, -1, 5, -1, 6, -1], 
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1], 
                    [-1, 6, -1, 7, -1, 8, -1, 9, -1], 
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1]]))

############################################################################################################

def affiche_laby(matrice):
    """
    Affiche le labyrinthe de maniere compréhensible pour l'utilisateur
    """
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j]==-1:
                print("* ",end="")
            elif matrice[i][j]==-2:
                print(". ",end="")
            elif matrice[i][j]==-3:
                print("A ",end="")
            elif matrice[i][j]==-4:
                print("B ",end="")
            else:
                print("  ",end="")
        print("")
        
print(affiche_laby([[-1, -1, -1, -1, -1, -1, -1, -1, -1], 
                    [-1, 0, 0, 0, 0, 0, 0, 0, -1], 
                    [-1, 0, -1, 0, -1, 0, -1, -1, -1], 
                    [-1, 0, -1, 0, -1, 0, 0, 0, -1], 
                    [-1, 0, -1, -1, -1, 0, -1, -1, -1], 
                    [-1, 0, 0, 0, -1, 0, 0, 0, -1], 
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1]]))

############################################################################################################

def check_depart(matrice,cases,x1,y1):
    """
    Fonction qui prend en argument la matrice, la liste des cases, les coordonnées du 
    départ et le nombre de cases différentes adjacentes au départ.
    Elle renvoie vrai si les coordonnées sont valides, faux sinon
    """
    print(matrice,cases,x1,y1)
    try:
        if y1==0 or y1==len(matrice)-1: #Si le départ est dans le mur du haut ou du bas
            if x1>0 and x1<len(matrice[y1]): #Si le départ a une abscisse valide
                return True
        if x1==0 or x1==len(matrice[y1])-1: #Si le départ est le mur de droite ou de gauche
            if y1>0 and y1<len(matrice): #Si le départ a une ordonnée valide
                return True
    except:
        return False
    return False
    
print(check_depart([[-1, -1, -1, -1, -1, -1, -1], 
                    [-1, 0, -1, 0, -1, 0, -1], 
                    [-1, 0, -1, 0, -1, 0, -1], 
                    [-1, 0, -1, 0, -1, 0, -1], 
                    [-1, 0, -1, 0, -1, 0, -1], 
                    [-1, 0, 0, 0, 0, 0, -1], 
                    [-1, -1, -1, -1, -1, -1, -1]],
                    [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, 
                     -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],0,1))

############################################################################################################

def check_arrivee(matrice,cases,x2,y2):
    """
    Fonction qui prend en argument la matrice, la liste des cases, les coordonnées de 
    l'arrivée et le nombre de cases différentes adjacentes à l'arrivée.
    Elle renvoie vrai si les coordonnées sont valides, faux sinon
    """
    try:
        if y2==0 or y2==len(matrice)-1: #Si l'arrivée est dans le mur du haut ou du bas
            if x2>0 and x2<len(matrice[y2]): #Si l'arrivée a une abscisse valide
                return True
        if x2==0 or x2==len(matrice[y2])-1: #Si l'arrivée est le mur de droite ou de gauche
            if y2>0 and y2<len(matrice): #Si l'arrivée a une ordonnée valide
                return True
    except:
        return False
    return False
    
print(check_arrivee([[-1, -1, -1, -1, -1, -1, -1], 
                    [-1, 0, -1, 0, -1, 0, -1], 
                    [-1, 0, -1, 0, -1, 0, -1], 
                    [-1, 0, -1, 0, -1, 0, -1], 
                    [-1, 0, -1, 0, -1, 0, -1], 
                    [-1, 0, 0, 0, 0, 0, -1], 
                    [-1, -1, -1, -1, -1, -1, -1]],
                    [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, 
                     -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],0,1))
                     
############################################################################################################
                     
