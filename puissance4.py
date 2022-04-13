import pathlib
import site

# Python je te hais de maniére passionelle; je suis pas censé faire ca :(
# (Ceci est une sorte de hack pas fou)
relative_home = pathlib.Path(__file__).parent.absolute()
module_home = relative_home.joinpath("modules")
site.addsitedir(module_home)

# -----------------------------------------------

from modules.p4_basesdedonnee import *
from modules.p4_console import *
from modules.p4_game import *
from modules.p4_ia import *
from modules.p4_network import *

def main():
    fin_partie = False
    game = P4_game()
    console = P4_console()
    db = p4_basesdedonnee()
    mode_de_jeu, difficulte = console.debut_jeu()
    
    if mode_de_jeu == 1:
        while fin_partie is not True:
            # Mise a jour de l'affichage
            console.modif_score(game)
            console.affiche(game.plateau_ligne_par_ligne())
            
            # Faire jouer le joueur
            while True:
                colonne = console.demander_colonne(1)
                if game.jeu_possible(colonne):
                    game.placer(colonne)
                    break

            fin_partie = game.victoire()
        
            # Faire jouer l'IA
            colonne = calculer_meilleur_move(game, difficulte, 2)
            if not game.jeu_possible(colonne):
                raise RuntimeError("Uh Oh: , l'IA a tentée de jouer sur une colonne interdite")
            game.placer(colonne)

            print(game.plateau)
            fin_partie = game.victoire()

    if mode_de_jeu == 2:
        while fin_partie is not True:
            # Mise a jour de l'affichage
            console.modif_score(game)
            console.affiche(game.plateau_ligne_par_ligne())

            # Faire jouer le joueur
            while True:
                tour = game.get_tour()
                colonne = console.demander_colonne(tour)
                if game.jeu_possible(colonne):
                    game.placer(colonne)
                    break
            
            fin_partie = game.victoire()

    if mode_de_jeu == 3:
        print("marche pas encore")

main()

#console.modif_score(game)
#db.ajoutdejoueuroumodificationdelabasededonee(console.j1['nom'], console.j1['score'])
#db.ajoutdejoueuroumodificationdelabasededonee(console.j2['nom'], console.j2['score'])
#db.recupererlesmeilleursscores()
