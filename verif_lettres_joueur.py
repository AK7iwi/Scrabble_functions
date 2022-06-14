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









