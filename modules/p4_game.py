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
        for _ in range(nb_line):
            nvline = []
            for _ in range(nb_col):
                nvline.append(0)
            self.plateau.append(nvline)
    
    def jeu_possible(self,col):
        """
        entré: numero de la colonne (1 à 7)
        sortie: print erreur si:
        -le numéro de la colonne est inférieur à 1,
        -supérieur à 6
        -si la la colonne est pleine
        sinon print "Le coup est possible"
        """
        if col < 1 or col > nb_col and len(self.plateau[col]) >= 7:
            print("ERREUR")
        else:
            print("Le coup est possible")
             

    def get_case(self,line,col):
        pass

    def victoire(self):
        pass
