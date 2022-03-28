import tkinter as tk
 

VD = 0  # case vide
J1 = 1  # case sélectionnée par le joueur 1
J2 = 2  # case sélectionnée par le joueur 2
INACTIF = 0
EN_COURS = 1
FINI = 2
 
# texte à afficher - couleur - couleur au survol
APPARENCE = {
    J1: ('1', '#EE5555', '#FF6666'),
    J2: ('2', '#5555EE', '#6666FF'),
    VD: ('x', '#222222', '#444444')
}
 
def initialiser_les_donnees(d, c):
    pass
 
def coup_valide(d, c, x):
    return True
 
