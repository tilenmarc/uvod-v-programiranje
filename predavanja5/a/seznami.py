def produkt_elementov(sez):
    produkt = 1
    for el in sez:
        produkt *= el

    return produkt


def najvecji_element_matrike(mat):
    """Poisce najvecji element v matriki,
    ki je predstavljena kot seznam seznamov."""

    maksimum = None
    for vrstica in mat:
        for el in vrstica:
            if maksimum == None or el > maksimum:
                maksimum = el

    return maksimum


def indeks_najvecjega(sez):
    maksimum = None
    indeks = None
    for i in range(len(sez)):
        el = sez[i]
        if maksimum == None or el > maksimum:
            maksimum = el
            indeks = i

    return indeks


def sled_matrike(mat):
    if len(mat) == 0:
        return 0

    el = mat[0][0]

    nova_matrika = []
    for vrstica in mat[1:]:
        nova_matrika = nova_matrika + [vrstica[1:]]

    return el + sled_matrike(nova_matrika)


def sled_matrike_bolje(mat):
    sled = 0

    for i in range(len(mat)):
        sled += mat[i][i]

    return sled


def sodi_elementi(sez):
    """Vrne nov seznam, ki vsebuje samo sode elemente danega sezanam."""
    nov_seznam = []
    for el in sez:
        if el % 2 == 0:
            nov_seznam.append(el)

    return nov_seznam


def sodi_elementi_pocasi(sez):
    """Vrne nov seznam, ki vsebuje samo sode elemente danega sezanam."""
    nov_seznam = []
    for el in sez:
        if el % 2 == 0:
            nov_seznam += nov_seznam + [el]

    return nov_seznam


def kvadrati(n):
    """Vrne seznam [1, 2**2, 3**2,...,n**2]"""
    sez = []
    for i in range(1, n + 1):
        sez.append(i**2)

    return sez


def kvadrati2(n):
    """Vrne seznam [1, 2**2, 3**2,...,n**2]"""
    return [i**2 for i in range(1, n + 1)]


def matrika_nicel(n, m):
    return [m * [0] for _ in range(n)]


def obrni_seznam(sez):
    """Obrne vrsni red elemento v seznamu."""
    nov_seznam = []
    for i in range(len(sez) - 1, -1, -1):
        nov_seznam.append(sez[i])

    for i in range(len(sez)):
        sez[i] = nov_seznam[i]


def obrni_seznam_inline(sez):
    """Obrne vrsni red elemento v seznamu."""
    for i in range(len(sez) // 2):
        sez[i], sez[-i - 1] = sez[-i - 1], sez[i]
