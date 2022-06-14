def propose_mot(msg_position_ligne, msg_position_colonne, msg_direction, msg_mot):

    ligne = -1000
    colonne = -1000
    NB_LIGNES = 15 #A modifier en fonction de la dimension du plateau
    NB_COLONNES = 15 #A modifier en fonction de la dimension du plateau

    while ligne < 0 or ligne > (NB_LIGNES - 1) or type(ligne) != int:
        ligne = int(input(msg_position_ligne))

    while colonne < 0 or colonne > (NB_COLONNES - 1) or type(colonne) != int:
        colonne = int(input(msg_position_colonne))

    while lettre.upper() != "V" and lettre.upper() != "H":
        lettre = str(input(msg_direction))

    while mot.isalpha() == False:
        mot = str(input(msg_mot))

    return (mot, (ligne, colonne), lettre)