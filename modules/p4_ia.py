# Ce Module implémente l' Intelligence Artificielle 
# du jeu, le tout sera fait par une simple fonction; 
# en se servant du MinMax
import random
COLONNES = 7
LIGNES = 6

DIFFICULTE_ALEATOIRE = 0
DIFFICULTE_FACILE = 1

def calculer_meilleur_move(plateau, difficulte):
    """
    Calcule le meilleur mouvement a jouer pour un plateau donné

    Entree :
     - `plateau`: Object 'P4_game'
     - `difficulté`: Représente le niveau de difficulté; peut etre;
        - 0: Aléatoire: Choisit une case au hasard
        - 1: Facile: Un algorithme de MinMax facile

    Sortie : Le numero de colonne sur lequel il faut placer le pion controllé par l'IA
    """
    # HAHA COMMENT C NUL
    if difficulte == DIFFICULTE_ALEATOIRE:
        return random.randint(0, COLONNES)
    
    if difficulte == DIFFICULTE_FACILE:
        raise "Pas encore implémenté"

