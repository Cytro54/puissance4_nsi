#variables principales
j1 = {}
j2 = {}

from p4_game import *
from p4_basesdedonnee import *


class p4_console:
    def __init__(self):
        pass
    def affiche(self,plateau):
        print(f"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓     Score {j1['nom']} : {j1['score']}")
        print(f"┃         Puissance 4       ┃     Score {j2['nom']} : {j2['score']}")
        print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
        for i in plateau:
            print("┃ ", end="")
            for y in range(len(i)):
                if i[y] == 0 :
                    print("___┃", end="")
                if i[y] == 1 :
                    print(f"{j1['motif']}┃", end="")
                if i[y] == 2 :
                    print(f"{j2['motif']}┃", end="")
                print(" ┃")
                print("┃━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┃")
        print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
        print("┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

#classe joueur
class joueur:
    def __init__(self):
        pass

    def debut_jeu(self):

        nb_joueurs = 0
        while nb_joueurs != 1 or nb_joueurs != 2 :
            print("Mode de jeux :")
            print("1: joueur contre IA")
            print("2: joueur contre joueur")
            nb_joueurs = int(input())
            if nb_joueurs != 1 or nb_joueurs != 2 :
                print("erreur")
        if nb_joueurs == 1 :
            j1["nom"] = input("nom du joueur :")
            j2["nom"] = "Viktor Nikiforov"    
            j1["score"] = 0
            j2["score"] = 0
            lmotif = ["⯀","⯁","⯂","⯄","⯅"]
            print("motif du joueur 1 :")
            for i in range(len(lmotif)):
                print(f"{i} : {lmotif[i]}")
            motif1 = lmotif[int(input())]
            lmotif.remove(motif1)
            print("motif de L'IA :")
            for i in range(len(lmotif)):
                print(f"{i} : {lmotif[i]}")
            motif2 = lmotif[int(input())]
            j1["motif"] = motif1
            j2["motif"] = motif2

        if nb_joueurs == 2 :
            j1["nom"] = input("nom du joueur 1 :")
            j2["nom"] = input("nom du joueur 2 :")
            j1["score"] = 0
            j2["score"] = 0
            lmotif = ["⯀","⯁","⯂","⯄","⯅"]
            print("motif du joueur 1 :")
            for i in range(len(lmotif)):
                print(f"{i} : {lmotif[i]}")
            motif1 = lmotif[int(input())]
            lmotif.remove(motif1)
            print("motif du joueur 2 :")
            for i in range(len(lmotif)):
                print(f"{i} : {lmotif[i]}")
            motif2 = lmotif[int(input())]
            j1["motif"] = motif1
            j2["motif"] = motif2






