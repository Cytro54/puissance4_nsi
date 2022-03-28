import tkinter as tk
 

VD = 0  # case vide
J1 = 1  # case sélectionnée par le joueur 1
J2 = 2  # case sélectionnée par le joueur 2
INACTIF = 0
EN_COURS = 1
FINI = 2


for ligne in range(5):
    for colonne in range(5):
        Button(fenetre, text='Ls-Cs' (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)