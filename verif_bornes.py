def verif_bornes(coup, dimensions):
    m = True
    if coup[2] == "h":
        if len(coup[0]) + coup[1][1] - 1 >= dimensions[0]:
            m = False

    if coup[2] == "v":
        if len(coup[0]) + coup[1][0] - 1 >= dimensions[1]:
            m = False
    return m
