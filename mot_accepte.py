def mot_accepte(plateau, lettres_joueur, coup, dico, tour):
    mot = coup[0]

    dimensions = (15, 15)

    def verif_premier_tour(coup):
        p = False
        if coup[2].lower() == "v":
            if coup[1][0] - 1 == 7 and coup[1][1] == 7:
                p = True
            if coup[1][1].lower() == 7:
                if coup[1][0] - 1 <= 7 or coup[1][0] >= 7 - len(coup[0]):
                    p = True

        if coup[2] == "h":
            if coup[1][1] - 1 == 7 and coup[1][1] == 7:
                p = True
            if coup[1][0] == 7:
                if coup[1][1] - 1 <= 7 or coup[1][1] >= 7 - len(coup[0]):
                    p = True
        return p

    def verif_lettres_joueur(plateau, lettres_joueur, coup):
        p = False
        a = 0
        for i in coup[0]:
            if i.upper() in lettres_joueur:
                a = a + 1
            elif not i in lettres_joueur:
                if i.upper() in plateau:
                    if coup[2].lower() == "h":
                        if i in plateau[coup[1][0]]:
                            a = a + 1

                        else:
                            a = a + 0
                    elif coup[2].lower() == "v":
                        if i in plateau[coup[1][1]]:
                            a = a + 1
                        else:
                            a = a + 0
                if not i.upper() in plateau:
                    a = a + 0

        if a >= len(coup[0]) - 2:
            p = True
        return p

    def verif_mot(mot, dico):
        p = False
        if mot.upper() in dico[len(mot) - 1]:
            p = True
        return p

    def verif_bornes(coup, dimensions):
        p = True
        if coup[2] == "h":
            if len(coup[0]) + coup[1][1] - 1 >= dimensions[0]:
                p = False

        if coup[2] == "v":
            if len(coup[0]) + coup[1][0] - 1 >= dimensions[1]:
                p = False
        return p

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

    if tour == 1:
        if verif_premier_tour(coup) == True:
            if verif_bornes(coup, dimensions) == True:
                if verif_lettres_joueur(plateau, lettres_joueur, coup) == True:
                    if verif_mot(mot, dico) == True:
                        if verif_emplacement(coup, plateau) == True:
                            return True
    if tour > 1:
        if verif_bornes(coup, dimensions) == True:
            if verif_lettres_joueur(plateau, lettres_joueur, coup) == True:
                if verif_mot(mot, dico) == True:
                    if verif_bornes(coup, dimensions) == True:
                        if verif_emplacement(coup, plateau) == True:
                            return True
    return False






