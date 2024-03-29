def prestej_pojavitve(niz):
    """Presteje, kolikokrat se pojavi vsak crka
    v nizu."""

    pojavitve = {}

    for znak in niz:
        if not znak.isalnum():
            continue
        elif znak not in pojavitve:
            pojavitve[znak] = 1
        else:
            pojavitve[znak] += 1

    return pojavitve


# slovar = {"knjiga": "book", "telefon": "phone", "blabla": "book"}

# for kljuc in slovar:
#     print(kljuc, slovar[kljuc])

# for vrednost in slovar.values():
#     print(vrednost)

# for kljuc, vrednost in slovar.items():
#     print(kljuc, vrednost)


def kljuc_najvecje_vrednosti(slovar):
    kljuc_najvecje = None
    najvecja_vrednost = None

    for kljuc, vrednost in slovar.items():
        if kljuc_najvecje == None:
            kljuc_najvecje = kljuc
            najvecja_vrednost = vrednost

        elif najvecja_vrednost < vrednost:
            najvecja_vrednost = vrednost
            kljuc_najvecje = kljuc

    return kljuc_najvecje


redka = ({(0, 0): 1, (1, 1): 4}, 3, 3)


def iz_redke_matrike_navadno(redka_matrika):
    navadna_matrika = []
    stevilo_vrstic = redka_matrika[1]
    stevilo_stolpcev = redka_matrika[2]
    matrika = redka_matrika[0]

    for i in range(stevilo_vrstic):
        vrstica = []
        for j in range(stevilo_stolpcev):
            if (i, j) in matrika:
                vrstica.append(matrika[(i, j)])
            else:
                vrstica.append(0)
        navadna_matrika.append(vrstica)

    return navadna_matrika


def iz_redke_matrike_navadno2(redka_matrika):
    navadna = []
    stevilo_vrstic = redka_matrika[1]
    stevilo_stolpcev = redka_matrika[2]
    matrika = redka_matrika[0]
    for _ in range(stevilo_vrstic):
        navadna.append(stevilo_stolpcev * [0])

    for kljuc, vrednost in matrika.items():
        navadna[kljuc[0]][kljuc[1]] = vrednost

    return navadna


def iz_navadne_v_redko_matriko(navadna_matrika):
    stevilo_vrstic = len(navadna_matrika)
    stevilo_stolpcev = len(navadna_matrika[0])

    matrika = {}
    for i, vrstica in enumerate(navadna_matrika):
        for j, vrednost in enumerate(vrstica):
            if vrednost != 0:
                matrika[(i, j)] = vrednost
    return (matrika, stevilo_vrstic, stevilo_stolpcev)
