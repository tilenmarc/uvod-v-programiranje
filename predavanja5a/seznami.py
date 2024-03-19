def produkt(sez):
    """Vrne produkt elementov seznama."""
    # for index in range(len(sez)):
    #     element = sez[index]

    produkt = 1
    for element in sez:
        produkt *= element

    return produkt


# matrika = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def sled_pocasi(matrika):
    """Vrne sled, to je vsoto diagonalnih elementov."""

    sled = 0

    for indeks1 in range(len(matrika)):
        for indeks2 in range(len(matrika[indeks1])):
            if indeks1 == indeks2:
                sled += matrika[indeks1][indeks2]

    return sled


def sled_hitro(matrika):
    """Vrne sled, to je vsoto diagonalnih elementov."""

    sled = 0

    for indeks in range(len(matrika)):
        sled += matrika[indeks][indeks]

    return sled


def najvecji_element(sez):
    if len(sez) == 0:
        return None

    najvecji = sez[0]

    # for indeks in range(len(sez)):
    #     element = sez[indeks]
    #     if element > najvecji:
    #         najvecji = element

    for element in sez:
        if element > najvecji:
            najvecji = element

    return najvecji


def sodi_elementi(sez):
    """Vrne nov seznam, katerega elementi so samo sodi
    elementi prvega."""

    nov_seznam = []

    for element in sez:
        if element % 2 == 0:
            nov_seznam.append(element)

    return nov_seznam


def sodi_elementi_pocasi(sez):
    """Vrne nov seznam, katerega elementi so samo sodi
    elementi prvega."""

    nov_seznam = []

    for element in sez:
        if element % 2 == 0:
            nov_seznam = nov_seznam + [element]

    return nov_seznam


def konstantna_matrika(c, n, m):
    """Vrne n x m matriko, katere vhodi so c."""

    vrstica = m * [c]
    matrika = []

    for _ in range(n):
        matrika.append(vrstica.copy())

    return matrika


# for indeks, element in enumerate(sez):


def funkcija_ki_vrne_dve_stvari():
    return 1, 2
