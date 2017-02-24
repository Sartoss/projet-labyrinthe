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
            elif matrice[i][j]==-2:
                print(". ",end="")
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


def check_depart(matrice,cases,x1,y1,dispos):
    """
    Fonction qui prend en argument la matrice, la liste des cases, les coordonnées du 
    départ et le nombre de cases différentes adjacentes au départ.
    Elle renvoie vrai si les coordonnées sont valides, faux sinon
    """
    if len(dispos)>0: #S'il y a une case adjacente au départ
        if y1==0 or y1==len(matrice)-1: #Si le départ est dans le mur du haut ou du bas
            if x1>0 and x1<len(matrice[y1]): #Si le départ a une abscisse valide
                return True
        if x1==0 or x1==len(matrice[y1])-1: #Si le départ est le mur de droite ou de gauche
            if y1>0 and y1<len(matrice): #Si le départ a une ordonnée valide
                return True
    return False
    

def check_arrivee(matrice,cases,x2,y2,dispos):
    """
    Fonction qui prend en argument la matrice, la liste des cases, les coordonnées de 
    l'arrivée et le nombre de cases différentes adjacentes à l'arrivée.
    Elle renvoie vrai si les coordonnées sont valides, faux sinon
    """
    if len(dispos)>0: #S'il y a une case adjacente à l'arrivée
        if y2==0 or y2==len(matrice)-1: #Si l'arrivée est dans le mur du haut ou du bas
            if x2>0 and x2<len(matrice[y2]): #Si l'arrivée a une abscisse valide
                return True
        if x2==0 or x2==len(matrice[y2])-1: #Si l'arrivée est le mur de droite ou de gauche
            if y2>0 and y2<len(matrice): #Si l'arrivée a une ordonnée valide
                return True
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
        dispos=cases_adjacentes(len(matrice),len(matrice[0]),y1*len(matrice[0])+x1,cases)[0]
        depok=check_depart(matrice,cases,x1,y1,dispos) #vérifie que le départ est bien placé
        if depok==False:
            print("Coordonnées invalides")
            
    while arrok==False:
        print("Entrer les coordonnées du point d'arrivée:")
        x2=int(input("X: ")) #abscisse de l'arrivée
        y2=int(input("Y: ")) #ordonnée de l'arrivée
        dispos=cases_adjacentes(len(matrice),len(matrice[0]),y2*len(matrice[0])+x2,cases)[0]
        arrok=check_arrivee(matrice,cases,x2,y2,dispos) #vérifie que l'arrivée est bien placée
        if arrok==False:
            print("Coordonnées invalides")
            
    return x1,y1,x2,y2


def determine_orientation(x1,y1,x,y):
    if x1-x==0:
        if y1-y==1:
            orient="bas"
        else:
            orient="haut"
    elif x1-x==1:
        orient="droite"
    else:
        orient="gauche"
    return orient
    
    
def direction(orient):
    if orient=="haut":
        direction=["droite","haut","gauche","bas"]
    elif orient=="droite":
        direction=["haut","gauche","bas","droite"]
    elif orient=="bas":
        direction=["gauche","bas","droite","haut"]
    elif orient=="gauche":
        direction=["bas","droite","haut","gauche"]
    return direction
    
    
def deplacement(direct,x1,y1):
    for i in range(4):
        if direct[i]=="droite" and matrice[y1][x1+1]!=-1:
            return [x1+1,y1]
        elif direct[i]=="gauche" and matrice[y1][x1-1]!=-1:
            return [x1-1,y1]
        elif direct[i]=="haut" and matrice[y1-1][x1]!=-1:
            return [x1,y1-1]
        elif direct[i]=="bas" and matrice[y1+1][x1]!=-1:
            return [x1,y1+1]


def deplacement_main_droite(matrice,x1,y1,x2,y2,cases):
    x=x1
    y=y1
    dep=y1*len(matrice[0])+x1
    case=cases_adjacentes(len(matrice),len(matrice[0]),dep,cases)[1][0]
    direct=dep-case
    if direct==1:
        x1-=1
    elif direct==-1:
        x1+=1
    elif direct==len(matrice[0]):
        print("yolo")
        y1-=1
    elif direct==-len(matrice[0]):
        y1+=1
    matrice[y1][x1]=-2
    while [x1,y1]!=[x2,y2]:
        print("yola")
        orient=determine_orientation(x1,y1,x,y)
        direct=direction(orient)
        x,y=x1,y1
        coords=deplacement(direct,x1,y1)
        print(coords)
        print(type(coords))
        x1=coords[0]
        y1=coords[1]
        matrice[y1][x1]=-2
    affiche_laby(matrice)


        
h,l=entree_infos_laby()
matrice=genere_matrice(h,l)
matrice=genere_laby(h,l,matrice)
affiche_laby(matrice)
cases=[]
for i in range(len(matrice)): #génère la liste des cases
    cases+=matrice[i]
x1,y1,x2,y2=entree_infos_chemin(matrice,cases)
matrice[y1][x1]=10
matrice[y2][x2]=11
affiche_laby(matrice)
deplacement_main_droite(matrice,x1,y1,x2,y2,cases)   
