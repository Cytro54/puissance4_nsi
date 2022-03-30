import P4_game

class p4_console:
    def __init__(self):

    def affiche(self,plateau):
        print("╭---------------------╮")
        print("|     Puissance 4     |")
        print("|---------------------|")
        for i in plateau:
            print("| ", end="")
            for y in range(len(i)):
                if i[y] == 0
                    print('__ ', end="")
                if i[y] == 1
                    print(f'{joueur.j1.motif} ', end="")
                if i[y] == 2
                    print(f'{joueur.j2.motif} ', end="")
                print(" |", end="")
        print("╰---------------------╯")

#classe joueur
class joueur:
    def __init__(self):
        pass
    def j1(self,motif,nom_joueur)
        self.motif = motif
    def j2(self,motif,nom_joueur)
        self.motif = motif
    def gagne(self,nom_joueur):
        self.score +=1




