from random import*

def entree_infos_laby():
    """
    Fonction qui fait entrer par l'utilisateur les dimensions du labyrinthe
    Elle renvoie la hauteur et la largeur du labyrinthe
    """
    l=int(input("Entrez les dimensions du labyrinthe :\nLargeur :"))
    h=int(input("Hauteur :"))
    return (h,l)

def genere_matrice(h,l):
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
    p=[" ","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j]==-1:
                print("* ",end="")
            else:
                print(p[matrice[i][j]]+" ",end="")
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


def entree_infos_chemin():
    """
    Fonction qui fait entrer par l'utilisateur les coordonnées de départ et d'arrivée du labyrinthe
    Elle renvoie les coordonnées du départ et de l'arrivée
    """
    print("Entrer les coordonnées du point de départ:")
    x1=int(input("X: ")) #abscisse du départ
    y1=int(input("Y: ")) #ordonnée du départ
    print("Entrer les coordonnées du point d'arrivée:")
    x2=int(input("X: ")) #abscisse de l'arrivée
    y2=int(input("Y: ")) #ordonnée de l'arrivée
    return [x1,y1],[x2,y2]
        
h,l=entree_infos_laby()
matrice=genere_matrice(h,l)
matrice=genere_laby(h,l,matrice)
affiche_laby(matrice)        
