#variable principale
nb_lignes = 6
nb_collonnes = 7
nb_lignes_gagnant = 4
nb_joueurs = 2
vide, joueur1, joueur2 = 0, 1, 2

Class jeu():
    def __init__(self):
        self.grille = []
        for ligne in range(nb_lignes+2): # +2 cases pour les bords
            self.grille.append(nb_collonnes+2) # +2 cases pour les bords
        joueur1 = joueur(rouge,nom_joueur1)
        joueur2 = joueur(jaune,nom_joueur2)