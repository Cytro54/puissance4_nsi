# Ce Module implémente l' Intelligence Artificielle 
# du jeu, le tout sera fait par une simple fonction; 
# en se servant du MinMax
import random
COLONNES = 7
LIGNES = 6
LONGEUR_LIGNE_VICTORIEUSE = 4
CASE_NEUTRE = 0

DIFFICULTE_ALEATOIRE = 0
DIFFICULTE_FACILE = 1

def __estimer_avantage(plateau, joueur, ligne, colonne, longueur):

    #    . . . . . 
    #    . 0 X X X
    #    0 X 0-0-0
    
    somme = 0
    if longueur == 0:
        return 0
    if plateau[ligne][colonne] == joueur:
        somme += 1
    if plateau[ligne][colonne] == joueur or plateau[ligne][colonne] == CASE_NEUTRE:
        
        somme += __estimer_avantage(plateau, joueur, ligne - 1, colonne - 1, longueur - 1)
        somme += __estimer_avantage(plateau, joueur, ligne - 1, colonne, longueur - 1)
        somme += __estimer_avantage(plateau, joueur, ligne - 1, colonne + 1, longueur - 1)

        somme += __estimer_avantage(plateau, joueur, ligne + 1, colonne - 1, longueur - 1)
        somme += __estimer_avantage(plateau, joueur, ligne + 1, colonne, longueur - 1)
        somme += __estimer_avantage(plateau, joueur, ligne + 1, colonne + 1, longueur - 1)     
        
        somme += __estimer_avantage(plateau, joueur, ligne, colonne - 1, longueur - 1)
        somme += __estimer_avantage(plateau, joueur, ligne, colonne + 1, longueur - 1)

        return somme
    else:
        return 0

def __estimer_avantages(plateau, joueur):
    somme = 0
    for ligne in range(0, LIGNES):
        for colone in range(0, COLONNES):
            somme += __estimer_avantage(plateau, joueur, ligne, colone, LONGEUR_LIGNE_VICTORIEUSE)

def __dump_plateau(game):
    tableau = [[0 for col in range(COLONNES)] for ligne in range(LIGNES)]
    for ligne in range(0, LIGNES):
        for col in range(0, COLONNES):
            tableau[ligne][col] = game.get_case(ligne, col)
    return tableau


def calculer_meilleur_move(game, difficulte):
    """
    Calcule le meilleur mouvement a jouer pour une game donné

    Entree :
     - `game`: Object 'P4_game'
     - `difficulté`: Représente le niveau de difficulté; peut etre;
        - 0: Aléatoire: Choisit une case au hasard
        - 1: Facile: Un algorithme de MinMax facile

    Sortie : Le numero de colonne sur lequel il faut placer le pion controllé par l'IA
    """
    if difficulte == DIFFICULTE_ALEATOIRE:
        return random.randint(0, COLONNES)
    
    if difficulte == DIFFICULTE_FACILE:
        raise "Pas encore implémenté"


# Asserts, Ou comment ne pas tester une IA
if __name__ == "__main__":
    PLATEAU_1 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    assert __estimer_avantage(PLATEAU_1, 1, 0, 0, 4) == 0