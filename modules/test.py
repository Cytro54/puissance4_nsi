#juste pour tester mon code
tour = 0
nb_line = 6
nb_col = 7


tour = 0
nb_line = 6
nb_col = 7
col = 1

plateau = [
    [0, 0, 0, 0, 0, 0],     # |
    [0, 0, 0, 0, 0, 0],     # | "Ligne"
    [0, 0, 0, 0, 0, 0],     # V
    [0, 0, 0, 0, 0, 0],     # + ----->
    [0, 0, 0, 0, 0, 0],     #    "Colonne"
    [0, 0, 0, 0, 0, 0],     #
]

print(plateau)

if tour % 2 == 0:

    for i in plateau[col]:
        
        while plateau[col][i] >= nb_line:
            if len(plateau[col]) => 6
            
            if i != 0:
                plateau[col][i-1] = 1
            else:
                pass
    tour +=1

else:
    for i in plateau[col]:
        while plateau[col][i] >= nb_line:
            if i != 0:
                plateau[col][i-1] = 2
            else:
                pass
    tour +=1