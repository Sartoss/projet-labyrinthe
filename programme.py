def entree_infos_laby():
    """
    Fonction qui fait entrer par l'utilisateur les dimensions du labyrinthe
    Elle renvoie la hauteur et la largeur du labyrinthe
    """
    l=int(input("Entrez les dimensions du labyrinthe :\nLargeur :"))
    h=int(input("Hauteur :"))
    return [h,l]

def genere_cases(h,l):
    matrice=[[-1]*(2*l+1)]
    for i in range(h):
        liste=[-1]
        for j in range(l):
            liste.append(l*i+j)
            liste.append(-1)
        matrice.append(liste)
        matrice.append([-1]*(2*l+1))

        
        

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
