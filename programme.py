def entree():
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
    for i in matrice:
        print(i)
        
        

def entree_infos_chemin():
    print("Entrer les coordonnées du point de départ:")
    x1=int(input("X: "))
    y1=int(input("Y: "))
    print("Entrer les coordonnées du point d'arrivée:")
    x2=int(input("X: "))
    y2=int(input("Y: "))
    return [x1,y1],[x2,y2]
