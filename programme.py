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


def entree_infos_chemin(matrice):
    """
    Fonction qui fait entrer par l'utilisateur les coordonnées de départ et d'arrivée du labyrinthe
    Elle renvoie les coordonnées du départ et de l'arrivée
    """
    cases=[]
    for i in range(len(matrice)):
        cases+=matrice[i]
    while True:
        print("Entrer les coordonnées du point de départ:")
        x1=int(input("X: ")) #abscisse du départ
        y1=int(input("Y: ")) #ordonnée du départ
        if y1==0 or y1==len(matrice)-1:
            if x1>0 and x1<len(matrice[y1]) and cases_adjacentes(len(matrice),len(matrice[0]),y1*len(matrice[0])+x1,cases):
                break
        if x1==0 or x1==len(matrice[y1])-1:
            if y1>0 and y1<len(matrice) and cases_adjacentes(len(matrice),len(matrice[0]),y1*len(matrice[0])+x1,cases):
                break
        print("Coordonnées invalides")
    
    while True:
        print("Entrer les coordonnées du point d'arrivée:")
        x2=int(input("X: ")) #abscisse de l'arrivée
        y2=int(input("Y: ")) #ordonnée de l'arrivée
        if y2==0 or y2==len(matrice)-1:
            if x2>0 and x2<len(matrice[y2]) and cases_adjacentes(len(matrice),len(matrice[0]),y2*len(matrice[0])+x2,cases):
                break
        if x2==0 or x2==len(matrice[y2])-1 and cases_adjacentes(len(matrice),len(matrice[0]),y2*len(matrice[0])+x2,cases):
            if y2>0 and y2<len(matrice):
                break
        print("Coordonnées invalides")
    return x1,y1,x2,y2
        
h,l=entree_infos_laby()
matrice=genere_matrice(h,l)
matrice=genere_laby(h,l,matrice)
affiche_laby(matrice)
x1,y1,x2,y2=entree_infos_chemin(matrice)
matrice[y1][x1]=10
matrice[y2][x2]=11
affiche_laby(matrice)   
