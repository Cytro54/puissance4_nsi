#variables principales
j1 = {}
j2 = {}

from p4_game import *
from p4_basesdedonnee import *


class P4_console:
    '''
    classe qui fait des trucs comme afficher le plateau et c'est tout
    '''
    def __init__(self):
        pass
    #affiche le plateau de jeu
    def affiche(self,plateau):
        #affiche le haut du plateau, les joueurs et les scores
        print(f"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓     Score {j1['nom']} : {j1['score']}")
        print(f"┃         Puissance 4       ┃     Score {j2['nom']} : {j2['score']}")
        print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
        #commence a afficher la "vrai" partie du tableau
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
        #affiche le numéro des colonnes du plateau
        print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
        print("┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    def jouer(self,j,c,joueur):
        if joueur == "j1" :
            print(f"choisir une colonne où placer le jeton de {j1['nom']}")
        if joueur == "j2" :
            print(f"choisir une colonne où placer le jeton de {j2['nom']}")
        c = int(input())
        j.placer(c)

#classe joueur
class joueur:
    '''
    classe qui gere les joueurs
    '''
    def __init__(self):
        pass

    def debut_jeu(self):
        '''
        fait ce qui se passe au debut du jeu
        '''
        nb_joueurs = 0
        while nb_joueurs != 1 or nb_joueurs != 2 or nb_joueurs != 3:
            print("Mode de jeux :")
            print("1: joueur contre IA")
            print("2: joueur contre joueur")
            nb_joueurs = int(input())
            if nb_joueurs != 1 or nb_joueurs != 2 or nb_joueurs != 3:
                print("erreur")
        #si il y a 1 joueur contre une IA
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
        #si il y a 2 joueurs, demande is le jeu est en ligne ou en local
            #marche pas encore
        if nb_joueurs == 3:
            print("marche pas encore")     
        nb_joueurs == 2    
        #jcj local
        if nb_joueurs == 2:
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
        return nb_joueurs
    def modif_score(self,jeu):
        '''
        modifie les scores
        '''
        a, b = jeu.getscore()
        j1["score"] = a
        j2["score"] = b
