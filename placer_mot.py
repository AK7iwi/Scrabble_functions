def placer_mot(coup, plateau):
    ligne = coup[1][0]
    colonne = coup[1][1]
    mot = coup[0]
    p = ""
    if coup[2] == "h":
        for i in mot:
            if plateau[ligne][colonne] == "_":
                plateau[ligne][colonne] == i
                colonne += 1
            elif plateau[ligne][colonne] == i:
                p = p + i
                colonne += 1
            elif plateau[ligne][colonne] != i or plateau[ligne][colonne] != "_":
                return False

    if coup[2] == "v":
        for i in mot:
            if plateau[ligne][colonne] == "_":
                plateau[ligne][colonne] == i
                ligne += 1
            elif plateau[ligne][colonne] == i:
                p = p + i
                ligne += 1
            elif plateau[ligne][colonne] != i or plateau[ligne][colonne] != "_":
                return False
    return p