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
        self.plateau = []
        self.tour = 0 #si le tour est un nombre paire le joueur 1 joue, sinon c'est le joueur 2 qui joue  
        self.j1_score = 0
        self.j2_score = 0


    def jeu(self):
        """
        création du plateau de jeu rn 6*7
        """
        self.plateau = []
        for _ in range(nb_line):
            nvline = []
            for _ in range(nb_col):
                nvline.append(0)
            self.plateau.append(nvline)

        return self.plateau

    def get_case(self,line,col):
        return self.plateau[col][line]


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
            return False
        else:
            print("Le coup est possible")
            return True
             

    def placer(self,col):
        """
        entrée: le numéro de la colonne
        sortie: le jeton correspondant au joueurs 1 ou 2 serra ajouté au dessus des autres jetons de la colonne
        """
        if self.jeu_possible(col) == False:
            print("la colonne est pleine")

        elif self.tour % 2 == 0:
            for i in self.plateau[col]:
                while i >= nb_line:
                    if self.plateau[col][i] == 0:
                        self.plateau[col][i] = 1

            self.tour +=1

        else:
            for i in self.plateau[col]:
                while i >= nb_line:
                    if self.plateau[col][i] == 0:
                        self.plateau[col][i] = 2

            self.tour +=1
        return (self.tour, self.plateau)

    def victoire(self):
        """
        fonction qui va définir si le joueur 1 à gagné ou perdu
        """
        if self.tour % 2 == 0: #tour du joueur 1
            if p4_ia.a_gagne(self, 1) == True:
                self.j1_score += 1
            return p4_ia.a_gagne(self, 1)
        else: #tour du joueur 2
            if p4_ia.a_gagne(self, 2) == True:
                self.j2_score += 1
            return p4_ia.a_gagne(self, 2)


    
    def get_score(self):
        """
        renvoie le score des deux joueurs
        """
        return (self.j1_score, self.j2_score)

    def commetuveux(self):
        if self.tour % 2 == 0:
            return "j1"
        else:
            return "j2"