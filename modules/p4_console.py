from p4_game import *
from p4_basesdedonnee import *

MOTIF = [" X "," 0 "," ⯀ "," ⯁ "," ⯂ "," ⯄ "," ⯅ "]

class P4_console:
    '''
    classe qui fait des trucs comme afficher le plateau et c'est tout
    '''
    def __init__(self):
        self.j1 = {}
        self.j2 = {}
    #affiche le plateau de jeu

    def affiche(self,plateau):
        print()
        print()
        #affiche le haut du plateau, les joueurs et les scores
        print(f"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓     Score {self.j1['nom']} : {self.j1['score']}")
        print(f"┃         Puissance 4       ┃     Score {self.j2['nom']} : {self.j2['score']}")
        print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
        #commence a afficher la "vrai" partie du tableau
        for colonne in plateau:
            print("┃", end="")
            for hauteur in range(len(colonne)):
                
                if colonne[hauteur] == 0 :
                    print("___┃", end="")
                if colonne[hauteur] == 1 :
                    print(f"{self.j1['motif']}┃", end="")
                if colonne[hauteur] == 2 :
                    print(f"{self.j2['motif']}┃", end="")
            print("")
            print("┃━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┃")
        #affiche le numéro des colonnes du plateau
        print("┃━━━━━━━━━━━━━━━━━━━━━━━━━━━┃")
        print("┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    
    def demander_colonne(self, joueur):
        texte = ""
        if joueur == 1 :
            texte = f"Où placer le jeton de {self.j1['nom']} ? "
        if joueur == 2 :
            texte = f"Où placer le jeton de {self.j2['nom']} ? "
        return int(input(texte)) - 1
        
    def debut_jeu(self):
        '''
        fait ce qui se passe au debut du jeu
        '''
        nb_joueurs = 0
        while nb_joueurs != 1 and nb_joueurs != 2 and nb_joueurs != 3:
            print(" ==== Mode de jeu ==== ")
            print("1: joueur contre IA")
            print("2: joueur contre joueur en local")
            #print("3: joueur contre joueur en ligne")
            nb_joueurs = int(input())
            if nb_joueurs > 3:
                print("erreur")
        #si il y a 1 joueur contre une IA
        if nb_joueurs == 1 :
            self.j1["nom"] = input("nom du joueur :")
            self.j2["nom"] = "Viktor Nikiforov"    
            self.j1["score"] = 0
            self.j2["score"] = 0
            lmotif = MOTIF
            print("motif du joueur 1 :")
            for i in range(len(lmotif)):
                print(f"{i} : {lmotif[i]}")
            motif1 = lmotif[int(input())]
            lmotif.remove(motif1)
            print("motif de L'IA :")
            for i in range(len(lmotif)):
                print(f"{i} : {lmotif[i]}")
            motif2 = lmotif[int(input())]
            self.j1["motif"] = motif1
            self.j2["motif"] = motif2
            # Plus de choix de difficulté pour le moment
            diff = 1 # p4_ia.DIIFICULTE_FACILE
            #while diff != 1 and diff != 2:
            #    print("difficultée de l'IA")
            #    print("1 : facile")
            #    print("2 : difficile")
            #    diff = int(input())
            #    if diff != 1 or diff != 2:
            #        print("erreur")
            #if diff == 1:
            return nb_joueurs, diff
            #if diff == 2:
            #    return nb_joueurs, 0
        if nb_joueurs == 3:
            print("marche pas encore donc c'est du 1v1 en local")     
            nb_joueurs == 2    
        #jcj local
        if nb_joueurs == 2:
            self.j1["nom"] = input("nom du joueur 1 :")
            self.j2["nom"] = input("nom du joueur 2 :")
            self.j1["score"] = 0
            self.j2["score"] = 0
            lmotif = MOTIF
            print("motif du joueur 1 :")
            for i in range(len(lmotif)):
                print(f"{i} : {lmotif[i]}")
            motif1 = lmotif[int(input())]
            lmotif.remove(motif1)
            print("motif du joueur 2 :")
            for i in range(len(lmotif)):
                print(f"{i} : {lmotif[i]}")
            motif2 = lmotif[int(input())]
            self.j1["motif"] = motif1
            self.j2["motif"] = motif2
            return nb_joueurs, "ahahahahahah"
    
    def modif_score(self,jeu):
        '''
        modifie les scores
        '''
        a, b = jeu.get_score()
        self.j1["score"] = a
        self.j2["score"] = b

    def fin_de_partie(self, nom_basededonnee,joueurquiagagne):
        reponse = 0
        if joueurquiagagne == "j1":
            print(f"{self.j1['nom']} a gagné")
        elif joueurquiagagne =="j2":
            print(f"{self.j2['nom']} a gagné")
        else:
            print("égalité, personne n'a gagné")
        print()
        while reponse != 1 and reponse !=2:
            print("voullez vous rejouer ?")
            print("1: oui")
            print("2: non") 
            reponse = int(input())
        if reponse == 1:
            return "rejouer"
        if reponse == 2:           
            nom_basededonnee.ajoutdejoueuroumodificationdelabasededonee(self.j1['nom'], self.j1['score'])
            nom_basededonnee.ajoutdejoueuroumodificationdelabasededonee(self.j2['nom'], self.j2['score'])
            nom_basededonnee.afficherlesmeilleursscores()
            return "pasrejouer"
            
