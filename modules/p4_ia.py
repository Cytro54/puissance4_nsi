# Ce Module implémente l' Intelligence Artificielle 
# du jeu, le tout sera fait par une simple fonction; 
# en se servant du MinMax
import random
COLONNES = 7
LIGNES = 6

def calculer_meilleur_move(plateau):
    """
    Calcule le meilleur mouvement a jouer pour un plateau donné

    Entrée : Un plateau implémente par un tableau de tableau. 
    Sortie : Le numero de colonne sur lequel il faut placer le pion controllé par l'IA
    """
    # HAHA
    return random.randint(0, COLONNES)
