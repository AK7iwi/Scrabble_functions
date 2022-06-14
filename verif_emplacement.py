def verif_emplacement(coup, plateau):
    p = False
    ligne = coup[1][0]
    colonne = coup[1][1]
    mot = coup[0]
    a = 0
    if coup[2].lower() == "h":
        for i in mot:
            if plateau[ligne][colonne] == "_":
                colonne = colonne + 1
                a = a + 1
            elif plateau[ligne][colonne] != "_":
                if i == plateau[ligne][colonne]:
                    colonne = colonne + 1
                    a = a + 1

    elif coup[2].lower() == "v":
        for i in mot:
            if plateau[ligne][colonne] == "_":
                ligne = ligne + 1
                a = a + 1
            elif plateau[ligne][colonne] != "_":
                if i == plateau[ligne][colonne]:
                    ligne = ligne + 1
                    a = a + 1
    if a == len(mot):
        p = True
    return p

