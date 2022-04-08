import pathlib
import site
from turtle import clear

# Python je te hais de maniére passionelle; je suis pas censé faire ca :(
relative_home = pathlib.Path(__file__).parent.absolute()
module_home = relative_home.joinpath("modules")
site.addsitedir(module_home)


from modules.p4_basesdedonnee import *
from modules.p4_console import *
from modules.p4_game import *
from modules.p4_ia import *
from modules.p4_network import *
finpartie = False
p4g = P4_game()
p4c = P4_console()
p4b = p4_basesdedonnee()
plateau = p4g.jeu()
y, diff= p4c.debut_jeu()
if y == 1:
    while finpartie is not True:
        p4c.affiche(plateau)
        p4c.jouer(p4g, "j1")
        finpartie = p4g.victoire()
        c = calculer_meilleur_move(p4g,diff,2)
        p4c.jouer_ai(p4g, c)
        finpartie = p4g.victoire()
if y == 2:
    print("marche pas encore")

if y == 3:
    while finpartie is not True:
        p4c.affiche(plateau)
        a = p4g.commetuveux()
        p4c.jouer(p4g, a)
        finpartie = p4g.victoire()
p4c.modif_score(p4g)
p4b.ajoutdejoueuroumodificationdelabasededonee(p4c.j1['nom'], p4c.j1['score'])
p4b.ajoutdejoueuroumodificationdelabasededonee(p4c.j2['nom'], p4c.j2['score'])
p4b.recupererlesmeilleursscores()