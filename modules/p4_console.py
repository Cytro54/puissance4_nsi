class p4console:
    def __init__(self):

    def affiche(self,plateau):
        for i in plateau:
            for y in range(len(i)):
                if i[y] == 0
                    print('__ ', end="")
                if i[y] == 1
                    print(f'{self.joueur1.motif} ', end="")
                if i[y] == 2
                    print(f'{self.joueur2.motif} ', end="")


#classe joueur
class joueur:
    def __init__(self,couleur,motif,nom_joueur):
        self.couleur = couleur
        self.nom_joueur = nom_joueur
        self.score = 0
    def gagne(self,nom_joueur):
        self.score +=1




