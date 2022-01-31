from tkinter import *
from random import randrange

# - FONCTIONS ET PROCEDURES - #

# Calcule et dessine le nouveau tableau


def tableau():
    calculer()
    draw()
    window.after(1, tableau)

# Initialisation


def initialisation():
    for y in range(hauteur):
        for x in range(largeur):
            # on met les cellules mortes d'abord, et la variable temporaire à morte aussi.
            state[x][y] = mort
            temp[x][y] = mort
            cellule[x][y] = canvas.create_rectangle(
                (x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="gray", fill="white")  # création des rectangles blancs

    # On place au hasard environ 25% de cellules en vie (permet d'éviter qu'il n'y aie qu'1 seule cellule, et donc de ne rien produire)
    for i in range(largeur*hauteur//4):
        state[randrange(largeur)][randrange(hauteur)] = vivant

# On applique les règles


def calculer():
    for y in range(hauteur):
        for x in range(largeur):
            # on appelle la fonction permettant de connaître le nombre de voisins
            nombre_voisins = compte_voisins(x, y)

            # Règle 1 - Mort d'isolement
            # Si la cellule est vivante et qu'elle a un nombre de voisins inférieur à deux
            if state[x][y] == vivant and nombre_voisins < 2:
                temp[x][y] = mort  # alors elle meurt

            # Règle 2 - Toute cellule avec 2 ou 3 voisins survit.
            # Si une cellule est vivante et qu'elle a deux ou trois voisins
            if state[x][y] == vivant and (nombre_voisins == 2 or nombre_voisins == 3):
                temp[x][y] = vivant  # alors elle reste en vie

            # Règle 3 - Mort par surpopulation
            # si une cellule est vivante et qu'elle a plus de trois voisins
            if state[x][y] == vivant and nombre_voisins > 3:
                temp[x][y] = mort  # alors elle meurt

            # Règle 4 - Naissance
            # si une cellule est morte et qu'elle a trois voisins
            if state[x][y] == mort and nombre_voisins == 3:
                temp[x][y] = vivant  # alors elle nait (son état est à vivant)

    for y in range(hauteur):
        for x in range(largeur):
            # l'état prend la valeur de la variable temporaire, définis par les tests des quatre règles ci-dessus
            state[x][y] = temp[x][y]

# On compte les voisins en vie (tableau torique, voir plus haut)


def compte_voisins(x, y):
    nombre_voisins = 0  # compteur du nombre de voisins à 0

    # on teste si chaque cellule à un voisin selon les 8 directions

    # diagonale haut-gauche
    if state[(x-1) % largeur][(y+1) % hauteur] == 1:
        nombre_voisins += 1

    # haut
    if state[x][(y+1) % hauteur] == 1:
        nombre_voisins += 1

    # Diagonale haut-droite
    if state[(x+1) % largeur][(y+1) % hauteur] == 1:
        nombre_voisins += 1

    # gauche
    if state[(x-1) % largeur][y] == 1:
        nombre_voisins += 1

    # droite
    if state[(x+1) % largeur][y] == 1:
        nombre_voisins += 1

    # Diagonale bas-gauche
    if state[(x-1) % largeur][(y-1) % hauteur] == 1:
        nombre_voisins += 1

    # bas
    if state[x][(y-1) % hauteur] == 1:
        nombre_voisins += 1

    # diagonale bas-droite
    if state[(x+1) % largeur][(y-1) % hauteur] == 1:
        nombre_voisins += 1

    return nombre_voisins  # on retourne la valeur du nombre de voisins

# On dessine toute les cellules


def draw():
    for y in range(hauteur):
        for x in range(largeur):
            if state[x][y] == 0:  # si l'état est à 0 (donc cellule morte)
                couleur = "white"  # on met la couleur blanche
            else:  # sinon elle est vivante
                couleur = "red"  # donc on met la couleur rouge
            # application du changement de couleur
            canvas.itemconfig(cellule[x][y], fill=couleur)


# - TKINTER - #


# Définitions des variables
# Hauteur du tableau
hauteur = 25
# Largeur du tableau
largeur = 25
cote = 15  # Taille d'une cellule (fixe, car il ne sert à rien de la modifier)
vivant = 1  # L'état vivant est définit à 1 ("True")
mort = 0  # L'état mort est définit à 0 ("False")

# Créer les matrices
# utilisation des raccourcis python (non obligatoire mais pratique)
cellule = [[0 for row in range(hauteur)] for col in range(largeur)]
state = [[mort for row in range(hauteur)] for col in range(largeur)]
temp = [[mort for row in range(hauteur)] for col in range(largeur)]


# Rassemblement des fonctions et procédures pour faire le programme
window = Tk()
window.title("Jeu de la vie")
canvas = Canvas(window, width=cote*largeur, height=cote *
                hauteur, highlightthickness=0)
canvas.pack()

initialisation()
tableau()

window.mainloop()
