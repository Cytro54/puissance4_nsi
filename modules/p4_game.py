#variable principale
nb_line = 6
nb_col = 7
nb_winer_line = 4
nb_joueurs = 2
vide, joueur1, joueur2 = 0, 1, 2

class P4_game():
    def __init__(self):
        self.plateau = []
        self.tour = 0

    def jeu(self):
        for line in range(nb_line):
            nvline = []
            for col in range(nb_col):
                nvline.append(col * 0)
            self.plateau.append(nvline)
    
    def jeu_possible(self,incolonne):
        pass

    def get_case(self,ligne,colonnes):
        pass

    def victoire(self):
        pass
