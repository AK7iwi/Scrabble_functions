def pioche_init(occurences_lettres):
    a = []
    for i in occurences_lettres :
        b = occurences_lettres[i]
        for j in range (b) :
            a.append(i)
    a.sort()
    return a