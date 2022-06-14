def load_fichier_lettres(mon_fichier):

    mon_fichier = open(str(mon_fichier))
    ligne = mon_fichier.readlines()
    Dico1={}
    Dico2={}
    for i in ligne:
        liste = i.split()
        Dico1[liste[0]] = int(liste[1])
        Dico2[liste[0]] = int(liste[2])
    return Dico1, Dico2