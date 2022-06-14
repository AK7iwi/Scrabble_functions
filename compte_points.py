def compte_points(mot, points_lettres):
    a = 0
    for i in mot:
        a += points_lettres[i]
    return a
