def produkt(sez):
    """Izracuna produkt vseh elementov v
    seznamu."""
    prod = 1

    for element in sez:
        prod = prod * element

    return prod


def ali_vsebuje(x, sez):
    """Preveri ali je x v sez."""
    for element in sez:
        if element == x:
            return True

    return False


def indeks_najvecjega(sez):
    """Vrne indeks najvecjega elementa v
    seznamu."""

    najvecji = None
    indeks = None
    for i in range(len(sez)):
        element = sez[i]
        if najvecji == None or element > najvecji:
            najvecji = element
            indeks = i

    return indeks


matrika = [[1, 2, 3], [2, 3, 4], [5, 5, 5]]


def sled_matrike(mat):
    sled = 0

    for i in range(len(mat)):
        vrstica = mat[i]
        for j in range(len(vrstica)):
            if i == j:
                element = vrstica[j]
                sled += element

    return sled


def sled_matrike_bolje(mat):
    sled = 0
    for i in range(len(mat)):
        sled += mat[i][i]

    return sled


def matrika_nicel(n, m):
    matrika = []

    for _ in range(n):
        vrstica = m * [0]
        matrika.append(vrstica)

    return matrika


def sodi_elementi(sez):
    """Vrne nov seznam vseh sodih elementov
    v sez."""

    sodi = []
    for element in sez:
        if element % 2 == 0:
            sodi.append(element)

    return sodi


def sodi_elementi_slabse(sez):
    """Vrne nov seznam vseh sodih elementov
    v sez."""

    sodi = []
    for element in sez:
        if element % 2 == 0:
            sodi = sodi + [element]

    return sodi


def funkcija_ki_vraca_vec_stvari():
    for x, y in [(1, 2), (4, 3)]:
        print(x, y)

    return 42, "ni napake"
