from p4_game import *

class p4_console:
    def __init__(self):
        pass
    def affiche(self,plateau):
        print(f"╭--------------------╮     Score {joueur.j1.nom} : {joueur.j1.score}           ")
        print(f"|     Puissance 4    |     Score {joueur.j2.nom} : {joueur.j2.score}           ")
        print(f"|--------------------|                    ")
        for i in plateau:
            print("| ", end="")
            for y in range(len(i)):
                if i[y] == 0 :
                    print('__|', end="")
                if i[y] == 1 :
                    print(f'{joueur.j1.motif}|', end="")
                if i[y] == 2 :
                    print(f'{joueur.j2.motif}|', end="")
                print(" |", end="")
        print("╰--------------------╯")

#classe joueur
class joueur:
    def __init__(self):
        self.motif = ""
        self.score = 0
        self.nom = ""
    
    def j1(self,motif,nom_joueur):
        self.motif = motif
        self.nom = nom_joueur

    def j2(self,motif,nom_joueur):
        self.motif = motif
        self.nom = nom_joueur

    def gagne(self,nom_joueur):
        self.score +=1




