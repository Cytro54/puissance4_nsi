#variables principales
nb_line = 6
nb_col = 7
nb_winer_line = 4
nb_joueurs = 2
vide, joueur1, joueur2 = 0, 1, 2
j1_score = 0
j2_score =0

class P4_game():
   """
   classe qui va s'occuper de la creation du jeu
   """ 
    def __init__(self):
        self.plateau = []
        #si le tour est un nombre paire le joueur 1 joue, sinon c'est le joueur 2 qui joue  
        self.tour = 0

    def jeu(self):
        """
        création du plateau de jeu
        """
        for _ in range(nb_line):
            nvline = []
            for _ in range(nb_col):
                nvline.append(0)
            self.plateau.append(nvline)

        return self.plateau
    
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
        if self.tour % 2 == 0:
            for i in self.plateau[col]:
                while self.plateau[col][i] >= nb_line:
                    if i != 0:
                        self.plateau[col][i-1] = 1
                    else:
                        pass
            self.tour +=1

        else:
            for i in self.plateau[col]:
                while self.plateau[col][i] >= nb_line:
                    if i != 0:
                        self.plateau[col][i-1] = 2
                    else:
                        pass
            self.tour +=1
        return self.tour, self.plateau

    def victoire(self):
        pass
    
    def get_score(self):
        return j1_score, j2_score