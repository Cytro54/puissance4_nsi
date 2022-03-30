# ----- 1 - IMPORTATIONS ------------------------------------
 
import tkinter as tk
 
 
# ----- 2 - CONSTANTES --------------------------------------
 
# Codification des contenus 
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
 
 
# ----- 3 - FONCTIONS liées à la partie DONNEES --------------
 
def initialiser_les_donnees(d, c):
    '''Initialise toutes les variables correctement
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: param c (list)        :: le tableau "complément d'information"    
    :: return (None)         :: "procédure" Python
    .. effet de bord         :: modifie d et c
 
    :: exemple
    >>> td = [[J1, J1, J1], [J2, J2, J2]]
    >>> tc = [J2, FINI]
    >>> initialiser_les_donnees(td, tc)
    >>> td
    [[0, 0, 0], [0, 0, 0]]
    >>> tc
    [1, 1]
 
    '''
    pass
 
def coup_valide(d, c, x):
    '''Fonction booléenne qui analyse le coup du joueur, modifie les données et réponds True/False
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: param c (list)        :: le tableau "complément d'information"    
    :: param x (int)         :: l'indice de la colonne où le joueur veut poser son jeton    
    :: return (bool)         :: True si cliquer sur cette case est valide
    .. effet de bord         :: peut modifier d, c
 
    :: exemples
    >>> td = [[VD, VD, VD], [J1, J1, J1], [J2, J2, J2]]
    >>> tc = [J2, EN_COURS]
    >>> coup_valide(td, tc, 2)
    True
    >>> td
    [[0, 0, 2], [1, 1, 1], [2, 2, 2]]
    >>> tc
    [1, 1]
 
    '''
    return True
 
def trouver_ligne(d, c, x):
    '''Renvoie l'indice de la ligne où placer le jeton du joueur actif dans la colonne x
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: param c (list)        :: le tableau "complément d'information"    
    :: param x (int)         :: l'indice de la colonne où le joueur veut poser son jeton   
    :: return (int)          :: l'indice de la ligne, -1 si impossible car déjà plein
 
    :: exemples
    >>> td = [[VD, VD, VD], [VD, VD, VD], [J1, J1, J1], [J2, J2, J2]]
    >>> tc = [J2, EN_COURS]
    >>> trouver_ligne(td, tc, 2)
    1
    >>> td = [[VD, VD, J1], [VD, VD, J2], [J1, J1, J1], [J2, J2, J2]]
    >>> trouver_ligne(td, tc, 2)
    -1
 
    '''
    # Méthode : on commence en bas et on cherche une case vide tant que l'indice de la ligne est bien >=0
    return 0
 
def ajouter_jeton(d, c, x, y):
    '''Placer le jeton du joueur actif dans la colonne x
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: param c (list)        :: le tableau "complément d'information"    
    :: param x (int)         :: l'indice de la colonne où le joueur veut poser son jeton
    :: param y (int)         :: l'indice de la ligne où le joueur peut poser son jeton
    :: return (None)         :: "procédure" Python 
    .. effet de bord         :: Modifie la matrice d si déplacement possible
 
    :: exemples
    >>> td = [[VD, VD, VD], [VD, VD, VD], [J1, J1, J1], [J2, J2, J2]]
    >>> tc = [J2, EN_COURS]
    >>> ajouter_jeton(td, tc, 1, 2)
    >>> td
    [[0, 0, 0], [0, 0, 0], [1, 2, 1], [2, 2, 2]]
    >>> ajouter_jeton(td, tc, 0, 0)
    >>> td
    [[2, 0, 0], [0, 0, 0], [1, 2, 1], [2, 2, 2]]
 
    '''
    pass
 
def est_plein(d):
    '''Fonction booléenne qui renvoie True si la matrice d est pleine
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: return (bool)         :: True si le joueur a gagné
 
    :: exemples
    >>> td = [[VD, J1, VD], [VD, J2, VD], [J1, J1, J1], [J2, J2, J2]]
    >>> est_plein(td)
    False
    >>> td = [[J2, J1, J2], [J1, J2, J2], [J1, J1, J1], [J2, J2, J2]]
    >>> est_plein(td)
    True
 
    '''
    return False
 
def est_victoire(d, c):
    '''Fonction booléenne qui teste si le joueur ACTIF a gagné
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: param c (list)        :: le tableau "complément d'information"
    :: return (bool)         :: True si le joueur a gagné
 
    :: exemples
    >>> td = [[VD, J1, J2, J2], [VD, J2, J2, VD], [J1, J1, J2, VD], [J2, J2, J2, VD]]
    >>> est_victoire(td, [J2, EN_COURS])
    True
    >>> est_victoire(td, [J1, EN_COURS])
    False
    >>> td = [[J1, J1, J1, J1], [VD, J2, J2, VD], [J1, J1, J2, VD], [J2, J2, J2, VD]]
    >>> est_victoire(td, [J1, EN_COURS])
    True
    >>> td = [[J1, VD, VD, VD], [VD, J1, J2, VD], [J1, J1, J1, VD], [J2, J2, J2, J1]]
    >>> est_victoire(td, [J1, EN_COURS])
    True
 
    '''
    return False
 
def est_victoire_verticale(d, c):
    '''Fonction booléenne qui teste si le joueur ACTIF a gagné sur une colonne
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: param c (list)        :: le tableau "complément d'information"
    :: return (bool)         :: True si le joueur a gagné
 
    :: exemples
    >>> td = [[VD, VD, J2, VD], [VD, VD, J2, VD], [VD, VD, J2, VD], [VD, VD, J2, VD], [J1, J1, J1, J1]]
    >>> est_victoire_verticale(td, [J2, EN_COURS])
    True
    >>> est_victoire_verticale(td, [J1, EN_COURS])
    False
    >>> td = [[VD, VD, J2, VD], [J2, J2, J2, J2], [J1, J1, J1, J1]]
    >>> est_victoire_verticale(td, [J2, EN_COURS])
    False
 
    '''
    return False
 
def est_victoire_horizontale(d, c):
    '''Fonction booléenne qui teste si le joueur ACTIF a gagné sur une ligne
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: param c (list)        :: le tableau "complément d'information"
    :: return (bool)         :: True si le joueur a gagné
 
    :: exemples
    >>> td = [[VD, VD, J2, VD], [VD, VD, J2, VD], [VD, VD, J2, VD], [VD, VD, J2, VD], [J1, J1, J1, J1]]
    >>> est_victoire_horizontale(td, [J2, EN_COURS])
    False
    >>> est_victoire_horizontale(td, [J1, EN_COURS])
    True
    >>> td = [[VD, VD, J2, VD], [J2, J2, J2, J2], [J1, J1, J1, J1]]
    >>> est_victoire_horizontale(td, [J2, EN_COURS])
    True
 
    '''
    return False
 
def est_victoire_diagonale(d, c):
    '''Fonction booléenne qui teste si le joueur ACTIF a gagné sur une ligne
 
    :: param d (list(list))  :: matrice contenant les données des cases
    :: param c (list)        :: le tableau "complément d'information"
    :: return (bool)         :: True si le joueur a gagné
 
    :: exemples
    >>> td = [[J1, VD, VD, J2], [VD, J1, J2, VD], [VD, J2, J1, VD], [J2, VD, VD, J1]]
    >>> est_victoire_diagonale(td, [J2, EN_COURS])
    True
    >>> td = [[J1, VD, VD, VD], [VD, J1, J2, VD], [VD, J2, J1, VD], [J2, VD, VD, J1]]
    >>> est_victoire_diagonale(td, [J1, EN_COURS])
    True
    >>> est_victoire_diagonale(td, [J2, EN_COURS])
    False
    >>> td = [[VD, VD, VD, VD], [J1, VD, VD, J2], [VD, J1, J2, VD], [VD, J2, J1, VD], [J2, VD, VD, J1]]
    >>> est_victoire_diagonale(td, [J2, EN_COURS])
    True
    >>> td = [[J1, VD, VD, VD], [VD, J1, J2, VD], [VD, J2, J1, VD], [J2, VD, VD, J1], [VD, VD, VD, VD]]
    >>> est_victoire_diagonale(td, [J1, EN_COURS])
    True
 
    '''
    return False
 
def changer_joueur(c):
    '''Modifie J1 en J2 et inversement
 
    :: param c (list)  :: le tableau "complément d'information"    
    :: return (None)   :: "procédure" Python 
    .. effet de bord   :: Modifie c[0]
 
    :: exemples ..
    >>> ct = [J1, EN_COURS]
    >>> changer_joueur(ct)
    >>> ct[0]
    2
    >>> changer_joueur(ct)
    >>> ct[0]
    1
 
    '''
    pass
 
def gerer_victoire(c):
    '''Modifie c pour gérer la victoire
 
    :: param c (list)  :: le tableau "complément d'information"    
    :: return (None)   :: "procédure" Python 
    .. effet de bord   :: Modifie c[1] à FINI
 
    :: exemples ..
    >>> ct = [J1, EN_COURS]
    >>> gerer_victoire(ct)
    >>> ct
    [1, 2]
    >>> ct = [J2, EN_COURS]
    >>> gerer_victoire(ct)
    >>> ct
    [2, 2]
 
    '''
    pass
 
def gerer_match_nul(c):
    '''Modifie c pour gérer un match nul
 
    :: param c (list)  :: le tableau "complément d'information"    
    :: return (None)   :: "procédure" Python 
    .. effet de bord   :: Modifie c[1] à FINI et c[0] à VD
 
    :: exemples ..
    >>> ct = [J1, EN_COURS]
    >>> gerer_match_nul(ct)
    >>> ct
    [0, 2]
    >>> ct = [J2, EN_COURS]
    >>> gerer_match_nul(ct)
    >>> ct
    [0, 2]
 
    '''
    pass
 
# ----- 4 - FONCTIONS liées à la partie INTERFACE -----------
 
def configurer_fenetre(fe):
    '''Procédure gérant les paramètres de la fenêtre reçue en paramètre
 
    :: param fe(tkinter.Tk) :: la référence d'une fenêtre de classe Tk    
    :: return (None) :: "procédure" Python
 
    '''
    fe.geometry("1200x600")
    fe.title("Puissance 4")
    fe.configure(bg="#CCCCCC")
 
def creer_cases(fe, d):
    '''Renvoie une matrice ayant les mêmes dimensions que dc et contenant des widgets Labels
 
    :: param fe(tkinter.Tk) :: la référence d'une fenêtre de classe Tk
    :: param d(list(list)) :: la matrice contenant les données des cases
    :: return (list(list)) :: matrice ayant les  dimensions d'entrée, contenant des tkinter.Label
 
    '''
    nbl = len(d)  # Nombre de lignes
    nbc = len(d[0])  # Nombre de lignes
 
    # On crée une matrice w qui servira à contenir les widgets représentant les cases
    w = [ [None for x in range(nbc)] for y in range(nbl) ]
 
    # On crée les Labels un par un et on les stocke dans la matrice
    for y in range(nbl):
        for x in range(nbc):
 
            # Calcul du numéro de la case
            numero = x + y * nbc
 
            # Création et stockage d'un Label
            w[y][x] = tk.Label(fe, text=numero, fg="white", bg='grey', width=10, height=5)
 
            # Affichage et placement du widget contenu dans w[y][x]
            px = 20 + x * 90  # position px en pixels      
            py = 20 + y * 85  # position py en pixels             
            w[y][x].place(x=px, y=py)
 
            # Option : rajout d'attributs pour les récupérer facilement
            w[y][x].numero = numero
            w[y][x].colonne = x
            w[y][x].ligne = y
 
            # Option : modification du widget (juste pour montrer qu'on peut !!)
            #if x == 1 :  # nous sommes sur la 2e colonne (indice 1)
            #    w[y][x].configure(bg='red')
            #elif y == 2 :  # nous sommes sur la 3e ligne (indice 2)
            #    w[y][x].configure(bg='#AA0000')
 
    # On renvoie la matrice
    return w
 
def modifier_apparence_case(case, v):
    '''Modifie l'apparence du widget en fonction de la valeur v
 
    :: param case (tkinter.Label) :: la référence du widget-case à modifier
    :: param v (int)              :: le code du contenu à afficher dans la case
    :: return (None) :: "procédure" Python
    .. effet de bord :: modifie le widget case
 
    '''
    if v in APPARENCE.keys():
        case.configure(text=APPARENCE[v][0])
        case.configure(bg=APPARENCE[v][1])
 
def modifier_apparence_cases(w, d):
    '''Modifie les widgets pour refléter les données du plateau de jeu
 
    :: param w (list(list)) :: matrice contenant les références des widgets
    :: param d (list(list)) :: matrice contenant les données des cases
    :: return (None) :: "procédure" Python
    .. effet de bord :: modifie la matrice w
 
    '''
    # On récupére les dimensions de la matrice d
    nbl = len(d)  # Nombre de lignes
    nbc = len(d[0])  # Nombre de lignes
 
    # On lit les données une par une et on modifie les widgets
    for y in range(nbl):
        for x in range(nbc):
            modifier_apparence_case(w[y][x], d[y][x])
 
def eclaircir(e, w, d):
    '''Modifie la case en utilisant la couleur claire
 
    :: param e (tkinter.Event) :: contient les informations sur l'événement
    :: param w (list(list))    :: matrice contenant les références des widgets
    :: param d (list(list))    :: matrice contenant les données des cases
    :: return (None)           :: "procédure" Python
    .. effet de bord           :: modifie la matrice w
 
    '''
    case = e.widget
    y = case.ligne
    x = case.colonne
    code = d[y][x]
    if code in APPARENCE:
        nouvelle_couleur = APPARENCE[code][2]
        case.configure(bg=nouvelle_couleur)
 
def assombrir(e, w, d):
    '''Modifie la case en utilisant la couleur sombre
 
    :: param e (tkinter.Event) :: contient les informations sur l'événement
    :: param w (list(list))    :: matrice contenant les références des widgets
    :: param d (list(list))    :: matrice contenant les données des cases
    :: return (None)           :: "procédure" Python
    .. effet de bord           :: modifie la matrice w
 
    '''
    case = e.widget
    y = case.ligne
    x = case.colonne
    code = d[y][x]
    if code in APPARENCE:
        nouvelle_couleur = APPARENCE[code][1]
        case.configure(bg=nouvelle_couleur)
 
def creer_zone_com(fe):
    '''Renvoie la référence d'un label Text servant à communiquer
 
    :: param fe(tkinter.Tk)   :: la référence d'une fenêtre de classe Tk
    :: return (tkinter.Label) :: la référence d'un widget tkinter.Label
 
    '''
    cm = tk.Label(fe, text="Nouveau jeu", fg="black", bg='grey', width=50, height=5)
    cm.place(x=750, y=50)
    return cm
 
def modifier_apparence_communication(cm, c):
    '''Modifie les widgets pour refléter les données du plateau de jeu
 
    :: param cm (tkinter.Label) :: le widget Label servant à communiquer
    :: param c (list)           :: le tableau "complément d'information"
    :: return (None) :: "procédure" Python
    .. effet de bord :: modifie le widget cm
 
    '''
    # A COMPLETER
 
    if c[1] == INACTIF:  #jeu non demarré
        texte = "Cliquer sur une case pour démarrer"
        couleur_fond = '#44AA44'
        cm.configure(text=texte)
        cm.configure(bg=couleur_fond)
 
def gerer_clic_case(e, w, d, c, cm):
    '''Choisit l'action à réaliser lorsqu'on clique sur le plateau
 
    :: param e (tkinter.Event) :: contient les informations sur l'événement
    :: param w (list(list))    :: matrice contenant les références des widgets
    :: param d (list(list))    :: matrice contenant les données des cases
    :: param c (list)           :: le tableau "complément d'information"    
    :: param cm (tkinter.Label) :: le widget Label servant à communiquer    
    :: return (None)           :: "procédure" Python
    .. effet de bord           :: peut modifier w, d, c et cm
 
    '''
    if c[1] == INACTIF or c[1] == FINI:  # le jeu n'a pas commencé ou est fini
        demarrer_jeu(w, d, c, cm)
    elif c[1] == EN_COURS:  # jeu en cours        
        gerer_nouveau_coup(e, w, d, c, cm)
 
def demarrer_jeu(w, d, c, cm):
    '''Initialise toutes les variables correctement
 
    :: param w (list(list))    :: matrice contenant les références des widgets
    :: param d (list(list))    :: matrice contenant les données des cases
    :: param c (list)           :: le tableau "complément d'information"    
    :: param cm (tkinter.Label) :: le widget Label servant à communiquer    
    :: return (None)           :: "procédure" Python
    .. effet de bord           :: peut modifier w, d, c et cm
 
    '''
    pass
 
def gerer_nouveau_coup(e, w, d, c, cm):
    '''Analyse le coup du joueur et modifie données et affichage en conséquence
 
    :: param e (tkinter.Event) :: contient les informations sur l'événement
    :: param w (list(list))    :: matrice contenant les références des widgets
    :: param d (list(list))    :: matrice contenant les données des cases
    :: param c (list)           :: le tableau "complément d'information"    
    :: param cm (tkinter.Label) :: le widget Label servant à communiquer    
    :: return (None)           :: "procédure" Python
    .. effet de bord           :: peut modifier w, d, c et cm
 
    '''
    case = e.widget
    x = case.colonne
    pass
 
 
# ----- 5 - PROGRAMME PRINCIPAL ------------------------------
 
if __name__ == '__main__' :
 
    # --- Activation des tests sur les fonctions du module
    import doctest
    # Pour tester toutes les fonctions :
    doctest.testmod()
    # Pour tester une fonction à la fois :
    # doctest.run_docstring_examples(initialiser_les_donnees, globals())
 
    # --- Données du jeu
 
    # informations diverses : 
    complement = [VD, INACTIF] # [0]: joueur actif, [1]: état du jeu
 
    # matrice encodant les données du plateau, C par défaut
    donnees = [
        [VD, VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD, VD]
    ]
 
    # --- Création de la fenêtre principale
    fenetre = tk.Tk()
    configurer_fenetre(fenetre)
 
    # --- Création des widgets représentant graphiquement les cases
    widgets = creer_cases(fenetre, donnees)
    modifier_apparence_cases(widgets, donnees)
 
    # --- Création du widget représentant graphiquement la zone de communication
    communication = creer_zone_com(fenetre)
    modifier_apparence_communication(communication, complement)
 
    # --- Création des événements
    nbl = len(widgets)
    nbc = len(widgets[0])
    for y in range(nbl):
        for x in range(nbc):
            widgets[y][x].bind('<Enter>', lambda event: eclaircir(event, widgets, donnees))
            widgets[y][x].bind('<Leave>', lambda event: assombrir(event, widgets, donnees))
            widgets[y][x].bind('<Button-1>', lambda event: gerer_clic_case(event, widgets, donnees, complement, communication))
 
    # --- Activation de la surveillance sur l'application graphique
    fenetre.mainloop()
