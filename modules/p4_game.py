#variable principale
nb_lignes = 6
nb_collonnes = 7
nb_lignes_gagnant = 4
nb_joueurs = 2
vide, joueur1, joueur2 = 0, 1, 2

Class jeu():
    def __init__(self):
        self.grille = []
        for ligne in range(nb_lignes+2):
            self.grille.append(nb_collonnes)