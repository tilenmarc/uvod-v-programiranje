def prva_zanka():
    while True:
        print("*******")


def druga_zanka(n):
    stevec = 0
    while stevec < n:
        print(stevec * "*")
        stevec += 1


def tretja_zanka(n):
    stevec = 0

    while True:
        while stevec < n:
            print(stevec * "*")
            stevec += 1

        while stevec >= 0:
            print(stevec * "*")
            stevec -= 1


def stevilo_clenov_harmonicne_vrste(x):
    """Presteje stevilo clenov harmonicne vrste,
    da vsota preseze x."""
    vsota = 0
    i = 1

    while vsota <= x:
        vsota += 1 / i
        i += 1

    return i - 1


def while_zanka(niz):
    i = 0
    while i < len(niz):
        print(f"Daj mi: {niz[i]}")
        i += 1


def for_zanka(niz):
    for crka in niz:
        print(f"Daj mi: {crka}")


def zanka_range(n):
    for i in range(n):
        print(i)


def zanka_range2(niz):
    for i in range(len(niz)):
        crka = niz[i]
        print(f"Daj mi: {crka}")


def fakulteta(n):
    i = 1
    produkt = 1
    while i <= n:
        produkt *= i
        i += 1

    return produkt


def fakulteta2(n):
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i

    return produkt


def stevilo_samoglasnikov(niz):
    vsota = 0
    for crka in niz:
        if crka in "aeiouAEIOU":
            vsota += 1

    return vsota


def zamenjaj_samoglasnike_z_vprasaji(niz):
    """Utvari nov niz, ki ima vprasaje namesto
    samoglasnikov."""
    nov_niz = ""

    for crka in niz:
        if crka in "aeiouAEIOU":
            nov_niz = nov_niz + "?"
        else:
            nov_niz = nov_niz + crka

    return nov_niz


import math


def nicla_sinusa(a, b, epsilon=1e-10):

    while b - a > epsilon:
        sredina = (a + b) / 2
        if math.sin(a) == 0:
            return a
        if math.sin(b) == 0:
            return b
        if math.sin(sredina) == 0:
            return sredina

        if math.sin(a) * math.sin(sredina) > 0:
            a, b = sredina, b
        else:
            a, b = a, sredina

    return sredina


def primer(n):
    for i in range(n):
        if i % 2 == 0:
            continue
        print(i)


def iscem_crko(niz, crka):
    najdba = False
    for e in niz:
        if e == crka:
            najdba = True
            break

    return najdba


def je_podniz(niz, podniz):
    for i in range(len(niz) - len(podniz) + 1):
        se_ujema = True
        for j in range(len(podniz)):
            if niz[i + j] != podniz[j]:
                se_ujema = False
                break
        if se_ujema:
            return True

    return False


def bla():
    pass
