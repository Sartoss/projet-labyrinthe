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
    
print(entree_infos_chemin([[-1, -1, -1, -1, -1, -1, -1], 
                           [-1, 0, -1, 0, -1, 0, -1], 
                           [-1, 0, -1, 0, -1, 0, -1], 
                           [-1, 0, -1, 0, -1, 0, -1], 
                           [-1, 0, -1, 0, -1, 0, -1], 
                           [-1, 0, 0, 0, 0, 0, -1], 
                           [-1, -1, -1, -1, -1, -1, -1]],
                           [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, 
                            -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1]))

############################################################################################################

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
    
print(genere_cycles(3,3,   [[-1, -1, -1, -1, -1, -1, -1], 
                           [-1, 0, -1, 0, -1, 0, -1], 
                           [-1, 0, -1, 0, -1, 0, -1], 
                           [-1, 0, -1, 0, -1, 0, -1], 
                           [-1, 0, -1, 0, -1, 0, -1], 
                           [-1, 0, 0, 0, 0, 0, -1], 
                           [-1, -1, -1, -1, -1, -1, -1]]))

############################################################################################################

def direction(orient):
    """
    Fonction qui, selon la direction précédente, définit l'ordre de priorité des murs
    à suivre
    Elle renvoie une liste ordonnée de ces murs, du plus au moins prioritairement suivi
    """
    if orient=="haut":
        direction=["droite","haut","gauche","bas"]
    elif orient=="gauche":
        direction=["haut","gauche","bas","droite"]
    elif orient=="bas":
        direction=["gauche","bas","droite","haut"]
    elif orient=="droite":
        direction=["bas","droite","haut","gauche"]
    return direction
    
print(direction("haut"))
print(direction("gauche"))
print(direction("bas"))
print(direction("droite"))

############################################################################################################

def deplacement(matrice,direct,x1,y1):
    """
    Fonction qui effectue le déplacement
    Elle renvoie les nouvelles coordonnées, la direction prise et le rang de priorité
    du mur suivi
    """
    for i in range(4):
        if direct[i]=="droite" and matrice[y1][x1+1]!=-1:
            return [x1+1,y1,"droite",i]
        elif direct[i]=="gauche" and matrice[y1][x1-1]!=-1:
            return [x1-1,y1,"gauche",i]
        elif direct[i]=="haut" and matrice[y1-1][x1]!=-1:
            return [x1,y1-1,"haut",i]
        elif direct[i]=="bas" and matrice[y1+1][x1]!=-1:
            return [x1,y1+1,"bas",i]

print(deplacement([[-1, -1, -1, -1, -1, -1, -1], 
                   [-1, 0, -1, 0, -1, 0, -1], 
                   [-1, 0, -1, 0, -1, 0, -1], 
                   [-1, 0, -1, 0, -1, 0, -1], 
                   [-1, 0, -1, 0, -1, 0, -1], 
                   [-1, 0, 0, 0, 0, 0, -1], 
                   [-1, -1, -1, -1, -1, -1, -1]],["droite","haut","gauche","bas"],1,1))

############################################################################################################

def chemin_ouvert(cases,l,h,dep,x1,y1):
    """
    Fonction qui trouve le numéro de la case adjacente au départ
    Elle renvoie ce numéro
    """
    if x1==0:
        return dep+1
    elif x1==l-1:
        return dep-1
    elif y1==0:
        return dep+l
    elif y1==h-1:
        return dep-l
        
print(chemin_ouvert([-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, 
                     -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
                     3,3,7,0,1))

############################################################################################################

def initialisation(matrice,cases,x1,y1):
    """
    Fonction qui effectue le premier déplacement
    Elle renvoie les coordonnées après ce déplacement
    """
    dep=y1*len(matrice[0])+x1 #donne le rang de la case de départ dans la liste cases
    case=chemin_ouvert(cases,len(matrice[0]),len(matrice),dep,x1,y1)
    direct=dep-case
    if direct==1: #vers la gauche
        x1-=1
        direct="gauche"
    elif direct==-1: #vers la droite
        x1+=1
        direct="droite"
    elif direct==len(matrice[0]): #vers le haut
        y1-=1
        direct="haut"
    elif direct==-len(matrice[0]): #vers le bas
        y1+=1
        direct="bas"
    return [x1,y1,direct]

print(initialisation([[-1, -1, -1, -1, -1, -1, -1], 
                      [-1, 0, -1, 0, -1, 0, -1], 
                      [-1, 0, -1, 0, -1, 0, -1], 
                      [-1, 0, -1, 0, -1, 0, -1], 
                      [-1, 0, -1, 0, -1, 0, -1], 
                      [-1, 0, 0, 0, 0, 0, -1], 
                      [-1, -1, -1, -1, -1, -1, -1]],
                      [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, 
                     -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
                     0,1))

############################################################################################################

def deplacement_main_droite(matrice,x1,y1,x2,y2,cases):
    """
    Fonction qui simule le déplacement dans le labyrinthe par la méthode de la main droite
    Elle retourne la matrice du labyrinthe modifiée avec le chemin de l'entrée à la sortie
    """
    coords=initialisation(matrice,cases,x1,y1) #récupère les coordonnées après le 1er déplacement
    x1=coords[0]
    y1=coords[1]
    orient=coords[2] #direction prise
    a=rang=0
    cases_visitees=[]
    while [x1,y1]!=[x2,y2]: #tant qu'on n'a pas atteint l'arrivée
        if rang==3: #demi-tour: on efface la point dans le cul-de-sac
            matrice[y][x]=0
        if matrice[y1][x1]==-2 or [x1,y1] in cases_visitees: #retour en arrière: on efface le chemin incorrect
            matrice[y1][x1]=0
        else: #nouveau chemin
            matrice[y1][x1]=-2
            cases_visitees.append([x1,y1])
            if a>0: #gère les virages où on passe plusieurs fois
                matrice[y][x]=-2
        x,y=x1,y1 #enregistre les coordonnées de la case précédente
        a+=1
        direct=direction(orient) #donne l'ordre de priorité des murs à suivre
        coords=deplacement(matrice,direct,x1,y1) #effectue le déplacement
        x1=coords[0]
        y1=coords[1]
        orient=coords[2]
        rang=coords[3]
    matrice[y][x]=-2
    return [matrice,a+1]

print(deplacement_main_droite([[-1, -1, -1, -1, -1, -1, -1], 
                               [-1, 0, -1, 0, -1, 0, -1], 
                               [-1, 0, -1, 0, -1, 0, -1], 
                               [-1, 0, -1, 0, -1, 0, -1], 
                               [-1, 0, -1, 0, -1, 0, -1], 
                               [-1, 0, 0, 0, 0, 0, -1], 
                               [-1, -1, -1, -1, -1, -1, -1]],
                               0,1,0,5,
                               [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, 
                                -1, 0, -1, 0, -1, 0, -1, -1, 0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1]))

############################################################################################################

