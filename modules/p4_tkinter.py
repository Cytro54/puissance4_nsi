import pygame
import sys
import time

pygame.init ()
image = pygame.image.load ("Puissance4.png")
sizeim = image.get_size ()
size = (sizeim[0]*1, sizeim[1])
screen = pygame.display.set_mode (size)
screen.blit (image, (0,0))
pygame.display.flip ()
 

M = [[0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0]]
 
joueur = 1
JetonsJoues = 0
P4 = False

# Fonctions 
def quel_joueur():
# Cette fonction retourne le numero du joueur qui doit jouer
    if (JetonsJoues % 2 == 0):
        jou = 1
    else:
        jou = 2
    return jou
 
def choisir_colonne(x,y):
# Cette fonction retourne la colonne demandee au joueur1
# Tant que la valeur n'est pas acceptable, on demande la colonne a jouer
    colo=x-16
    col=col/97
    if col in range(0,7):
        if (M[5][col]==0):
            test=False
    return col
 
def ligne():
# Cette fonction retourne la ligne vide correspondant a la colonne demandee
    lig = 0
    for i in range (1,6):
        if ( M[i][colonne] == 0 and M[i-1][colonne] != 0 ):
            lig = i
    return lig

 
def affichage(matrice):
    screen.fill((0,0,0))
    screen.blit(image,(0,0))
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j]==1:
                    screen.blit(pionrouge,(16+97*j,13-97.5*i+486))
                pygame.display.flip()
            if matrice[i][j]==2:
                    screen.blit(pionjaune,(16+97*j,13-97.5*i+486))
                pygame.display.flip()
 
 
pionjaune = pygame.image.load ("PionJaune.png")
pionrouge = pygame.image.load ("PionRouge.png")
font = pygame.font.Font ("freesansbold.ttf", 15)

 
while (not P4 and JetonsJoues < 42):
    time.sleep (0.1)
    # Le joueur joue
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP :
            x,y = pygame.mouse.get_pos()
            joueur = quel_joueur()
            colonne = choisir_colonne(x,y)
     # On modifie les variables pour tenir compte du jeton depose.
            M[ligne()][colonne] = joueur
            JetonsJoues = JetonsJoues + 1
            P4 = verification_P4()
            affichage(M)
            pygame.display.flip()
 
 
        if event.type == pygame.QUIT:
            sys.exit()