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
        return 0

    try:
        case = plateau[ligne][colonne]
    except IndexError:
        # En dehors du plateau ? ; la ligne s'arette ici.
        return 0

    if case != CASE_NEUTRE and case != joueur:
        # Si la case est pas neutre ou de nous, alors la ligne s'arette ici. 
        return 0

    if case == joueur:
        # La case est a nous :), ajoutons 1 au compteur
        somme += 1

    # Maintenant, calculons cette somme pour la case adjacente suivant le vecteur.
    #print(f"{norme_vecteur} > ({ligne},{colonne})")
    somme += __estimer_avantage_vectoriel(
        plateau, 
        joueur, 
        origine_ligne, 
        origine_colonne, 
        vecteur_ligne, 
        vecteur_colonne, 
        norme_vecteur)

    return somme

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
        ajout = __estimer_avantage_vectoriel(plateau, joueur, ligne, colonne, vecteur_ligne, vecteur_colonne, 0)
        if ajout >= LONGEUR_LIGNE_VICTORIEUSE:
            raise RuntimeWarning(f"Gagné : Depart de x({ligne}, {colonne}) Vecteur v({vecteur_ligne}, {vecteur_colonne})")
        else:
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
    tableau = [[0 for col in range(COLONNES)] for ligne in range(LIGNES)]
    for ligne in range(0, LIGNES):
        for col in range(0, COLONNES):
            tableau[ligne][col] = game.get_case(ligne, col)
    return tableau

def __mix_max(game, joueur):

    meilleur_avantage = 0
    meilleur_move = 0
    for col in range(COLONNES):
        # Comment perdre de la memoire en une étape.
        game_essaye = game.copy()
        if game_essaye.jeu_possible(col):
            game_essaye.placer(col)
            plateau_temporaire = __dump_plateau(game_essaye)
            avantage_temporaire = __estimer_avantages(plateau_temporaire, joueur)
            if avantage_temporaire > meilleur_avantage:
                meilleur_move = col
                meilleur_avantage = avantage_temporaire
    return meilleur_move

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
    if difficulte == DIFFICULTE_ALEATOIRE:
        return random.randint(0, COLONNES)
    
    if difficulte == DIFFICULTE_FACILE:
        return __mix_max(game, joueur_ia)


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
    except RuntimeWarning:
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
