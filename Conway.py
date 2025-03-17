import random
import time
from copy import deepcopy

def premiere_grille(taille):
    """
    Params :
        type_du_param : int
        a quoi il correspond : la nombre de lignes et de colones de la grille de notre jeu
    Returns :
        type_du_retour : liste de liste
        a quoi il correspond : grille générée de maniere aleatoire avec un taille donnée
    Que fait cette fonction : elle génére la premiere grille notre jeu de maniére aletoire
    """
    grille = [[random.choice(["□", "■"]) for i in range(taille)] for u in range(taille)]
    return grille

def affichage(grille):
    """
    Params :
        type_du_param : liste
        a quoi il correspond : elle stock toutes les "cellules" du jeu
    Returns :
        type_du_retour : none
        a quoi il correspond : rien
    Que fait cette fonction :  elle affiche la grille console avec des chaines de caractere
    """
    taille_de_ligne = 0
    for sous_liste in grille:
        for carré in sous_liste:
            print(carré, end= " ")
            taille_de_ligne = taille_de_ligne + 1
            if taille_de_ligne  == len(grille):
                taille_de_ligne = 0
                print()

def compter_voisins(grille, cordX, coordY):
    """
    Params :
        type_du_param : liste
                        int
                        int
        a quoi il correspond :  elle stock toutes les "cellules" du jeu
                                Cordonnées de la cellule dont on veut compter les voisins
    Returns :
        type_du_retour : int
        a quoi il correspond : nombre de voisins de la cellule étudiées
    Que fait cette fonction :  elle compte pour une cellule donnée le nombre de voisines vivantes (a partir de ses coordonnées)
    """
    voisins = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i==0 and j==0):
                if 0 <= cordX+i < len(grille) and 0 <= coordY+j < len(grille):
                    if grille[cordX+i][coordY+j] == "■":
                        voisins = voisins + 1
    return voisins

def gen_suivante (grille):
    """
    Params :
        type_du_param : liste
        a quoi il correspond : elle stock toutes les "cellules" du jeu
    Returns :
        type_du_retour : liste de liste
        a quoi il correspond : la nouvelle grille, apres aplication de regles du jeu de la vie
    Que fait cette fonction :  elle aplique les regles du Jeu de la Vie a la grille
    """
    new_grille = deepcopy(grille)
    for cordX in range(len(grille)):
        for coordY in range(len(grille)):
            voisins = compter_voisins(grille, cordX, coordY)
            if grille[cordX][coordY] == "■" and (voisins < 2 or voisins > 3):
                new_grille[cordX][coordY] = "□"
            elif grille[cordX][coordY] == "□" and voisins == 3:
                new_grille[cordX][coordY] = "■"
    return new_grille

def jeu_vie(taille, iterations):
    """
    Params :
        type_du_param : int
                        int
        a quoi il correspond :  le nombre de lignes et de colones de la grille de notre jeu
                                le nombre souhaité de générations
    Returns :
        type_du_retour : none
        a quoi il correspond /
    Que fait cette fonction : elle lance le jeu de la vie
    """
    grille = premiere_grille(taille)
    affichage(grille)

    for i in range(iterations):
        grille = gen_suivante(grille)
        time.sleep(0.5)
        print(" ")
        affichage(grille)

if __name__ == '__main__':
    jeu_vie(10, 10)