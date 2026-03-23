def najvecji(sez):
    maks = None

    for el in sez:
        if maks == None or el > maks:
            maks = el

    return maks


def indeks_najvecjega(sez):
    maks = None
    indeks = None
    for i in range(len(sez)):
        el = sez[i]
        if maks is None or el > maks:
            maks = el
            indeks = i

    return indeks


def sled_matrike(mat):
    vsota = 0
    for i in range(len(mat)):
        vsota += mat[i][i]

    return vsota


def konstantna_matrika(n, m, x):
    mat = []
    for _ in range(n):
        mat.append(m * [x])

    return mat


def konstantna_matrika2(n, m, x):
    return [m * [x] for _ in range(n)]


def uredi(sez):
    """Vrne nov seznam z elementi urejenimi po velikosti."""
    if sez == []:
        return []

    nov_sez = sez.copy()

    i = indeks_najvecjega(sez)

    del nov_sez[i]

    urejen = uredi(nov_sez)
    urejen.append(sez[i])

    return urejen


def bubble_sort(sez):
    while True:
        so_urejeni = True
        for i in range(len(sez) - 1):
            if sez[i] > sez[i + 1]:
                sez[i], sez[i + 1] = sez[i + 1], sez[i]
                so_urejeni = False

        if so_urejeni:
            break


import random

sez = [random.randint(0, 100000000) for _ in range(1000)]


def quicksort(sez):
    if len(sez) <= 1:
        return sez

    indeks = random.randint(0, len(sez) - 1)
    pivot = sez[indeks]

    manjsi = []
    vecji = []
    for i in range(len(sez)):
        if i == indeks:
            continue
        el = sez[i]
        if el >= pivot:
            vecji.append(el)
        else:
            manjsi.append(el)

    return quicksort(manjsi) + [pivot] + quicksort(vecji)
