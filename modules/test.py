plateau = []
tour = 0
for _ in range(6):
    nvline = []
    for _ in range(7):
        nvline.append(0)
    plateau.append(nvline)

print(plateau)



def jeu_possible(col):
    if col < 1 or col > 7 and len(self.plateau[col]) >= 7:
        print("ERREUR")
        return False
    else:
        print("Le coup est possible")
        return True

def placer(col):
    global tour
    if jeu_possible(col) == False:
        print("la colonne est pleine")

    elif tour % 2 == 0:
        for i in plateau[col]:
            while i >= 5:
                if plateau[col][i] == 0:
                    plateau[col][i] = 1

        tour +=1

    else:
        for i in plateau[col]:
            while i >= 5:
                if plateau[col][i] == 0:
                    plateau[col][i] = 2

        tour +=1
    return (tour, plateau)

placer(2)
print(plateau) 

