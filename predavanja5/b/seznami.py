def najvecji(sez):
    najvecji_element = None
    for element in sez:
        if najvecji_element == None or najvecji_element < element:
            najvecji_element = element

    return najvecji_element


def indeks_najvecjega(sez):
    najvecji_element = None
    indeks_najvecjega = None
    for i in range(len(sez)):
        element = sez[i]
        if najvecji_element == None or najvecji_element < element:
            najvecji_element = element
            indeks_najvecjega = i

    return indeks_najvecjega


def konstantna_matrika(x, n, m):
    matrika = []
    for i in range(n):
        matrika.append(m * [x])

    return matrika


def sodi_elementi(sez):
    """Vrne nov seznam, ki vsebuje sode
    elemente sez."""
    sodi = []

    for element in sez:
        if element % 2 == 0:
            sodi.append(element)

    return sodi


def sodi_elementi2(sez):
    """Vrne nov seznam, ki vsebuje sode
    elemente sez, a pocasnje."""
    sodi = []

    for element in sez:
        if element % 2 == 0:
            sodi += sodi + [element]

    return sodi


def obrni(sez):
    for i in range(len(sez) // 2):
        sez[i], sez[-i - 1] = sez[-i - 1], sez[i]


def uredi(sez):
    """Vrne nov urejen seznam."""
    nov_sez = sez.copy()

    urejen = []
    while len(nov_sez) > 0:
        i = indeks_najvecjega(nov_sez)
        urejen.append(nov_sez[i])
        del nov_sez[i]

    obrni(urejen)

    return urejen


import random


def quicksort(sez):
    if len(sez) <= 1:
        return sez

    i = random.randint(0, len(sez) - 1)
    pivot = sez[i]
    manjsi = []
    vecji = []

    for element in sez:
        if element < pivot:
            manjsi.append(element)
        if element > pivot:
            vecji.append(element)

    return quicksort(manjsi) + [pivot] + quicksort(vecji)
