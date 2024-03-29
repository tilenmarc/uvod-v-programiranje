def indeks_najvecjega_elementa(sez):
    if len(sez) == 0:
        return None

    najvecji = sez[0]
    indeks = 0

    for i, element in enumerate(sez):
        if element > najvecji:
            najvecji = element
            indeks = i

    return indeks


def sled_matrike(mat):
    """Vrne vsoto diagonalnih elementov
    kvadratne matrike."""

    sled = 0
    for indeks in range(len(mat)):
        sled += mat[indeks][indeks]

    # pocasna verzija:
    # for indeks1 in range(len(mat)):
    #     for indeks2 in range(len(mat)):
    #         if indeks1 == indeks2:
    #             sled += mat[indeks][indeks]

    return sled


def sodi_elementi(sez):
    """Vrne nov seznam, ki vsebuje sode elemente prvega."""
    sodi = []

    for element in sez:
        if element % 2 == 0:
            sodi.append(element)

    return sodi


def sodi_elementi_pocasi(sez):
    """Vrne nov seznam, ki vsebuje sode elemente prvega."""
    sodi = []

    for element in sez:
        if element % 2 == 0:
            sodi = sodi + [element]

    return sodi


def uredi_seznam(sez):
    """Vrne nov seznam urejenih elementov."""
    if len(sez) <= 1:
        return sez

    najmanjsi = min(sez)
    indeks = sez.index(najmanjsi)

    nov_seznam = [najmanjsi] + uredi_seznam(sez[0:indeks] + sez[indeks + 1 :])

    return nov_seznam


import random


def quicksort(sez):
    if len(sez) <= 1:
        return sez

    indeks = random.randint(0, len(sez) - 1)
    pivot = sez[indeks]

    manjsi = []
    vecji = []

    for el in sez:
        if el < pivot:
            manjsi.append(el)
        if el > pivot:
            vecji.append(el)

    return quicksort(manjsi) + [pivot] + quicksort(vecji)
