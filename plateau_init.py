def plateau_init(dimensions) :
    b = dimensions
    c = []
    d = []
    e = 0
    f = 0
    while e < b[1]:
        e = e +1
        c.append("_")
    while  f < b[0]:
        f = f +1
        d.append(c)
    return(d)