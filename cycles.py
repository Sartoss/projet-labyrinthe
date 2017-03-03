# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:55:29 2017

@author: piroulasau
"""

from random import*

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

def genere_matrice(h,l):
    """
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

def affiche_laby(matrice):
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

def check_depart(matrice,cases,x1,y1):
    """
    Fonction qui prend en argument la matrice, la liste des cases, les coordonnées du 
    départ et le nombre de cases différentes adjacentes au départ.
    Elle renvoie vrai si les coordonnées sont valides, faux sinon
    """
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


def entree_infos_chemin(matrice,cases):
    """
    Fonction qui fait entrer par l'utilisateur les coordonnées de départ et d'arrivée du labyrinthe
    Elle renvoie les coordonnées du départ et de l'arrivée
    """
    depok=False
    arrok=False  
    while depok==False:
        print("Entrer les coordonnées du point de départ:")
        x1=int(input("X: ")) #abscisse du départ
        y1=int(input("Y: ")) #ordonnée du départ
        depok=check_depart(matrice,cases,x1,y1) #vérifie que le départ est bien placé
        if depok==False or len(cases_adjacentes(len(matrice),len(matrice[0]),y1*len(matrice[0])+x1,cases)[0])==0:
            print("Coordonnées invalides")
            depok=False
            
    while arrok==False:
        print("Entrer les coordonnées du point d'arrivée:")
        x2=int(input("X: ")) #abscisse de l'arrivée
        y2=int(input("Y: ")) #ordonnée de l'arrivée
        arrok=check_arrivee(matrice,cases,x2,y2) #vérifie que l'arrivée est bien placée
        if arrok==False or len(cases_adjacentes(len(matrice),len(matrice[0]),y2*len(matrice[0])+x2,cases)[0])==0:
            print("Coordonnées invalides")
            arrok=False
            
    return x1,y1,x2,y2

def parcours(x,y,xa,ya,h,l,laby):
    arrivé=False
    c=1
    a=[[],[y*l+x]]
    while not arrivé:
        a[0]=a[1][:]
        a[1]=[]
        for i in a[0]:
            x=i%l
            y=i//l
            a[1]+=cases_adjacentes(h,l,y*l+x,laby)[1]
            l[y*l+x]=c
            if(x,y)==(xa,ya):
                arrivé=True
        c+=1
    return laby
    
def parcoursinv(x,y,xa,ya,h,l,laby):
    while (x,y)!=(xa,ya):
        for i in [(y-1)*l+x,y*l+x-1,y*l+x+1,(y+1)*l+x]:
            if laby[i]==laby[y*l+x]-1:
                laby[y*l+x]=-2
                x,y=i%l,i//l
                break  
    return laby

def genere_cycles(h,l,laby):
    """
    Fonction qui, à partir des dimensions et de la matrice du labyrinthe, y ajoute des cycles
    Elle renvoie  le labyrinthe ainsi complexifié
    """
    liste=[]
    for j in range(1,h-1): 
        for i in range(1,l-1):
            if laby[j][i]!=0 and(laby[j-1][i]==laby[j+1][i])and(laby[j][i-1]==laby[j][i+1])and(laby[j+1][i]!=laby[j][i-1]):
                liste.append([i,j])
    for k in range(h*l//50):
        c=liste.pop(randint(0,len(liste)-1))
        laby[c[1]][c[0]]=0
    return laby


def main():
    """
    Fonction principale du programme
    """        
    h,l=entree_infos_laby()
    matrice=genere_matrice(h,l)
    matrice=genere_laby(h,l,matrice)
    l=2*l+1
    h=2*h+1
    matrice=genere_cycles(h,l,matrice)
    print("Voici le labyrinthe aléatoire généré :")
    affiche_laby(matrice)
    cases=[]
    for i in range(len(matrice)): #génère la liste des cases
        cases+=matrice[i]
    x1,y1,x2,y2=entree_infos_chemin(matrice,cases)
    cases[(l)*y1+x1]=0
    cases[(l)*y2+x2]=0
    laby=parcours(x1,y1,x2,y2,h,l,cases)
    laby=parcoursinv(x2,y2,x1,y1,h,l,cases)
    cases[(l)*y1+x1]=-3
    cases[(l)*y2+x2]=-4
    matrice=[]
    for i in range(h):
        matrice.append(laby[(l)*i:(l)*(i+1)])
    print("Voici le plus court chemin :")
    affiche_laby(matrice)
main()
