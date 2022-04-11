import p4_ia
#variables principales

nb_line = 6 # hauteur du plateau
nb_col = 7 # largeur du plateau
nb_winer_line = 4 
nb_joueurs = 2
vide, j1, j2 = 0, 1, 2 # diférenciation des cases du joueur1, du joueur 2 et des cases vides

class P4_game():
    """
    classe qui va s'occuper de la création du jeu
    """ 
    def __init__(self):
        # Variables
        self.plateau = []
        self.tour = 0 #si le tour est un nombre pair le joueur 1 joue, sinon c'est le joueur 2 qui joue  
        self.j1_score = 0
        self.j2_score = 0

        # Creation du plateau
        self.plateau = []
        for _ in range(nb_col):
            nvcol = []
            for _ in range(nb_line):
                nvcol.append(0)
            self.plateau.append(nvcol)

    def plateau_ligne_par_ligne(self):
        plateau_lpl = []
        for id_ligne in range(nb_line -1, -1, -1):
            ligne = []
            for colonne in range(nb_col):
                ligne.append(self.get_case(id_ligne, colonne))
            plateau_lpl.append(ligne)
        
        return plateau_lpl

    def get_case(self,line,col):
        return self.plateau[col][line]


    def jeu_possible(self,col):
        """
        entrée: numero de la colonne (0 à 6)
        sortie: print erreur si:
        -le numéro de la colonne est inférieur à 1,
        -supérieur à 6
        -si la la colonne est pleine
        sinon print "Le coup est possible"
        """
        if col < 0 or col > (nb_col - 1):
            return False
        else:
            # ben voyons; on depasse pas les limites ici.
            somme_cases_non_nulles = 0
            for case in self.plateau[col]:
                if case != 0:
                    somme_cases_non_nulles += 1

            #print(f"scnn: {somme_cases_non_nulles}")
            if somme_cases_non_nulles >= 7:
                return False
            return True
    
    def __jeton_depuis_tour(self):
        if self.tour % 2 == 0:  # Tour du J1
            return 1
        else:                   # Tour du J2
            return 2

    def placer(self,col):
        """
        entrée: le numéro de la colonne
        sortie: le jeton correspondant au joueurs 1 ou 2 serra ajouté au dessus des autres jetons de la colonne
        """
        #print(f"self.plateau: {self.plateau}")
        if not self.jeu_possible(col):
            #print("la colonne est pleine")
            pass
        else:
            #print("jeu possible")
            self.__placer_colonne(col, self.__jeton_depuis_tour())
            self.tour +=1

        return (self.tour, self.plateau)

    def __placer_colonne(self, col, case):
        i = 0
        for case_sondee in self.plateau[col]:
            if case_sondee == 0:
                self.plateau[col][i] = case
                break
            i += 1

    def victoire(self):
        """
        fonction qui va définir si le joueur 1 à gagné ou perdu
        """
        j1_gagne = p4_ia.a_gagne(self, 1)
        if j1_gagne:
            self.j1_score += 1

        j2_gagne = p4_ia.a_gagne(self, 2)
        if j2_gagne:
            self.j2_score += 1

        return j1_gagne or j2_gagne
    
    def get_score(self):
        """
        renvoie le score des deux joueurs
        """
        return (self.j1_score, self.j2_score)

    def get_tour(self):
        if self.tour % 2 == 0:
            return 1
        else:
            return 2
