# Ce Module implémente l' "Intelligence Artificielle", 
# (elle s'appelle Viktor)
# du jeu, le tout sera fait par une simple fonction; 
# en se servant du MinMax
import random
from copy import copy, deepcopy
COLONNES = 7
LIGNES = 6
LONGEUR_LIGNE_VICTORIEUSE = 4
CASE_NEUTRE = 0
DEEP_LEVEL = 1

DIFFICULTE_ALEATOIRE = 0
DIFFICULTE_FACILE = 1

class VictoireException(Exception):
    """ Execption qui indique que l'on a gagné"""
    # HAHAHAHAHHAHAHAHHAHA MAIS QUESCAUE C NUl DHUFFRYUFGRYFGRYGFYRGFYU

def __estimer_avantage_vectoriel(
    plateau, 
    joueur, 
    origine_ligne, 
    origine_colonne,
    vecteur_ligne,
    vecteur_colonne, 
    norme_vecteur):

    ligne = origine_ligne + norme_vecteur * vecteur_ligne     
    colonne = origine_colonne + norme_vecteur * vecteur_colonne
    norme_vecteur += 1
    somme = 0
    
    if ligne < 0 or colonne < 0:
        # En dehors du plateau; 
        return (somme, norme_vecteur)

    try:
        case = plateau[ligne][colonne]
    except IndexError:
        # En dehors du plateau ? ; la ligne s'arette ici.
        return (somme, norme_vecteur)

    if case != CASE_NEUTRE and case != joueur:
        # Si la case est pas neutre ou de nous, alors la ligne s'arette ici. 
        return (somme, norme_vecteur)

    if case == joueur:
        # La case est a nous :), ajoutons 1 au compteur
        somme += 1

    # Maintenant, calculons cette somme pour la case adjacente suivant le vecteur.
    #print(f"{norme_vecteur} > ({ligne},{colonne})")
    (somme_ajout, norme_vecteur) = __estimer_avantage_vectoriel(
        plateau, 
        joueur, 
        origine_ligne, 
        origine_colonne, 
        vecteur_ligne, 
        vecteur_colonne, 
        norme_vecteur)

    somme += somme_ajout

    if somme >= LONGEUR_LIGNE_VICTORIEUSE and norme_vecteur == LONGEUR_LIGNE_VICTORIEUSE + 1:
        raise VictoireException(f"Gagné : Depart de x({ligne}, {colonne}) Vecteur v({vecteur_ligne}, {vecteur_colonne})")

    return (somme, norme_vecteur)

def __estimer_avantage(
    plateau, 
    joueur, 
    ligne, 
    colonne):

    #    . . . . . 
    #    . 0 X X X
    #    0 X 0-0-0
    somme = 0

    def estim_rapide(vecteur_ligne, vecteur_colonne):
        (ajout, _) = __estimer_avantage_vectoriel(plateau, joueur, ligne, colonne, vecteur_ligne, vecteur_colonne, 0)
        return ajout
            

    # Calculer pour toutes les lignes possibles

    somme += estim_rapide(0, 1)
    somme += estim_rapide(0, -1)

    somme += estim_rapide(1, 1)
    somme += estim_rapide(1, -1)
    somme += estim_rapide(1, 0)

    somme += estim_rapide(-1, 1)
    somme += estim_rapide(-1, -1)
    somme += estim_rapide(-1, 0)

    return somme

def __estimer_avantages(plateau, joueur):
    somme = 0
    for ligne in range(0, COLONNES - 1):
        for colonne in range(0, LIGNES - 1):
            if plateau[ligne][colonne] == joueur:
                somme += __estimer_avantage(plateau, joueur, ligne, colonne)

    return somme

def __dump_plateau(game):
    # Vu que la classe de plateau est aussi stable que la syrie, 
    # cette fonction risque de bouger souvent
    # (en gros, elle dump le plateau depuis les sombres objects de yanis 
    # ma propre représentation, tout aussi bizarre)
    return game.plateau

def __mini_max(game, profondeur, maximisant, joueur):
    if profondeur == 0:
        # Estimons notre avantage ici.
        try:
            avantage = __estimer_avantages(__dump_plateau(game), joueur)

            return None, avantage
        except VictoireException:
            # On gagne ou on perd !!!!!
            return None, float('inf')
            

    col = None
    print(f"{profondeur}")
    if maximisant:
        value = float('-inf')
        for col in range(COLONNES):
            next_game = deepcopy(game)
            next_game.placer(col)
            col_essai, value_essai = __mini_max(next_game, profondeur - 1, False, joueur)
            print(f"+ {col_essai} -> {value_essai}")
            if col_essai is None:
                col_essai = col
            if value_essai > value:
                value = value_essai
                col = col_essai
    else: # Joueur ennemi
        value = float('+inf')
        for col in range(COLONNES):
            next_game = deepcopy(game)
            next_game.placer(col)
            col_essai, value_essai = __mini_max(next_game, profondeur - 1, True, joueur)
            print(f"- {col_essai} -> {value_essai}")
            if col_essai is None:
                col_essai = col
            if value_essai < value:
                value = value_essai
                col = col_essai
    return col, value


def calculer_meilleur_move(game, difficulte, joueur_ia):
    """
    Calcule le meilleur mouvement a jouer pour une game donnée

    Entree :
     - `game`: Object 'P4_game'
     - `difficulté`: Représente le niveau de difficulté; peut etre;
        - 0: Aléatoire: Choisit une case au hasard
        - 1: Facile: Un algorithme de MinMax facile
     - `joueur_ia`: Identifiant du joueur joué par l'IA (1 ou 2)

    Sortie : Le numero de colonne sur lequel il faut placer le pion controllé par l'IA
    """
    if difficulte == DIFFICULTE_FACILE:
        col, _avantage = __mini_max(game, DEEP_LEVEL, True, joueur_ia)
        print(col)
        return col

def a_gagne(game, joueur):
    """
    Verifie si le joueur précisé a gagné

    Entree :
     - `game`: Object 'P4_game'
     - `joueur`: Le "numero de joueur" sur lequel on vérifie si il n'ya pas victoire.

    Sortie : Un boolean représentant si le joueur a gagné.
    """
    try:
        plateau = __dump_plateau(game)
        _avantage = __estimer_avantages(plateau, joueur)
        return False
    except VictoireException:
        return True

# Asserts, Ou comment ne pas tester une IA
if __name__ == "__main__":
    # Trucs utiles
    def assert_avantage(plateau, joueur_gagnant):
        avantage1 = __estimer_avantages(plateau, 1)
        avantage2 = __estimer_avantages(plateau, 2)
        print(f"Avantage 1: {avantage1}")
        print(f"Avantage 2: {avantage2}")
        if joueur_gagnant == 1:
            assert avantage1 >= avantage2
        if joueur_gagnant == 2:
            assert avantage2 >= avantage1

    
    # Jeu Nul
    PLATEAU_1 = [
        [0, 0, 0, 0, 0, 0],     # |
        [0, 0, 0, 0, 0, 0],     # | "Colonne"
        [0, 0, 0, 0, 0, 0],     # V
        [0, 0, 0, 0, 0, 0],     # + ----->
        [0, 0, 0, 0, 0, 0],     #    "Ligne"
        [0, 0, 0, 0, 0, 0],     #
    ]

    print(" == Plateau Nul == ")
    assert_avantage(PLATEAU_1, 1)

    # Jeu avec avantage pour 1
    PLATEAU_2 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0],
    ]

    print(" == Avantage de 1 == ")
    assert_avantage(PLATEAU_2, 1)

    # Jeu avec victoire pour 1
    PLATEAU_3 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0],
    ]

    print(" == Victoire de 1 == ")
    try:
        assert_avantage(PLATEAU_3, 1)
        raise "C'est censé crasher xd"
    except VictoireException:
        # Normalement; l'estimation deverait dire que il a gagné
        # Donc on s'attend a une erreur
        pass

    # Jeu random
    PLATEAU_3 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0],
    ]

    print(" == Autre jeu == ")
    assert_avantage(PLATEAU_3, 1)


    # Tests d'intégration avec le module p4Game
    import p4_game
    g = p4_game.P4_game()
    g.jeu()
    print(__dump_plateau(g)) # VERUFIER LES LONGEURS
    
