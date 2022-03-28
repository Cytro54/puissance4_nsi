#variable principale
nb_lignes = 6
nb_colonnes = 7
nb_lignes_gagnant = 4
nb_joueurs = 2
vide, joueur1, joueur2 = 0, 1, 2

class P4_game():
    def __init__(self):
        self.plateau = []
        for ligne in range(nb_lignes+2): # +2 cases pour les bords
            self.plateau.append(nb_colonnes+2) # +2 cases pour les bords
        self.tour = 0

    def jeu(self):
        pass
    
    def jeu_possible(self):
        pass

    def get_case(self,ligne,colonnes):
        pass

    def victoire(self):
        pass
