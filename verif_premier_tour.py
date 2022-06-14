def verif_premier_tour(coup):
    p = False
    if coup[2].lower() == "v":
        if coup[1][0] - 1 == 7 and coup[1][1] == 7:
            p = True
        if coup[1][1] == 7:
            if coup[1][0] - 1 <= 7 or coup[1][0] >= 7 - len(coup[0]):
                p = True

    if coup[2].lower() == "h":
        if coup[1][1] - 1 == 7 and coup[1][1] == 7:
            p = True
        if coup[1][0] == 7:
            if coup[1][1] - 1 <= 7 or coup[1][1] >= 7 - len(coup[0]):
                p = True
    return p