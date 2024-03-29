slovar = {"kljuc1": 1000, "kljuc2": 1000}


def zanke_s_slovarji(slovar):
    for kljuc in slovar:
        print("kljuc", kljuc)

    for vredost in slovar.values():
        print("vrednost", vredost)

    for kljuc, vrednost in slovar.items():
        print("kljuc", kljuc)
        print("vrednost", vredost)


def prestej_pojavitve(niz):
    pojavitve = {}

    for znak in niz:
        if znak not in pojavitve:
            pojavitve[znak] = 1
        else:
            pojavitve[znak] += 1

    return pojavitve


def kljuc_najvecje_vrednosti(slovar):
    najvecji_kljuc = None
    najvecja_vrednost = None

    for kljuc, vrednost in slovar.items():
        if najvecji_kljuc == None:
            najvecji_kljuc = kljuc
            najvecja_vrednost = vrednost
        elif vrednost > najvecja_vrednost:
            najvecji_kljuc = kljuc
            najvecja_vrednost = vrednost

    return najvecji_kljuc


def najpogostejsi_znak(niz):
    pojavitve = prestej_pojavitve(niz)
    znak = kljuc_najvecje_vrednosti(pojavitve)

    return znak


redka = ({(0, 0): 1, (1, 2): 2}, 3, 3)


def iz_redke_v_navadno_matriko(redka):
    stevilo_vrstic = redka[1]
    stevilo_stolpcev = redka[2]
    slovar = redka[0]

    matrika = []
    for i in range(stevilo_vrstic):
        vrstica = []
        for j in range(stevilo_stolpcev):
            if (i, j) in slovar:
                vrstica.append(slovar[(i, j)])
            else:
                vrstica.append(0)
        matrika.append(vrstica)

    return matrika
