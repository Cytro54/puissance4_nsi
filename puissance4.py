import pathlib
import site

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
p4j = joueur()
p4b = p4_basesdedonnee()
p4g.jeu()
y, diff= p4j.debut_jeu()
if y == 1:
    while finpartie is not True:
        p4c.affiche()
        p4c.jouer(p4g, "j1")
        finpartie = p4g.victoire()
        c = calculer_meilleur_move(p4g,diff,2)
        p4c.jouer_ai(p4g, c)
        finpartie = p4g.victoire()
if y == 2:
    print("marche pas encore")

if y == 3:
    while finpartie is not True:
        p4c.affiche()
        a = p4g.commetuveux()
        p4c.jouer(p4g, a)
        finpartie = p4g.victoire()
p4j.modif_score()
p4b.ajoutdejoueuroumodificationdelabasededonee(j1['nom'], j1['score'])
p4b.ajoutdejoueuroumodificationdelabasededonee(j2['nom'], j2['score'])
p4b.recupererlesmeilleursscores()