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
p4j.debut_jeu()
while finpartie is not True:
    p4c.affiche()
    a = p4g.commetuveux()
    p4c.jouer(p4g, a)
    finpartie = p4g.victoire()
p4j.modif_score()
p4b.recupererlesmeilleursscores()