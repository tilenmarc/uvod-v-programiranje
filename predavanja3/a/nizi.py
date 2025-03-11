def srednja_crka(niz):
    sredina = len(niz) // 2

    return niz[sredina]


def je_samoglasnik(znak):
    """Vrne True, ce je znak samoglasnik, sicer False."""

    if znak == "a" or znak == "e" or znak == "i" or znak == "u" or znak == "o":
        return True
    else:
        return False


def je_samoglasnik_lepse(znak):
    """Vrne True, ce je znak samoglasnik, sicer False."""

    if znak in "aeiouAEIOU":
        return True
    else:
        return False


def stevilo_samoglasnikov(niz):
    """Presteje stevilo samoglasnikov v nizu."""

    if len(niz) == 0:
        return 0

    stevilo_brez_prvega = stevilo_samoglasnikov(niz[1 : len(niz)])

    if je_samoglasnik_lepse(niz[0]):
        return stevilo_brez_prvega + 1
    else:
        return stevilo_brez_prvega


def zamenjaj_samoglasnike_z_vprasaji(niz):
    if niz == "":
        return ""

    podniz_zamenjan = zamenjaj_samoglasnike_z_vprasaji(niz[1 : len(niz)])

    if je_samoglasnik_lepse(niz[0]):
        return "?" + podniz_zamenjan
    else:
        return niz[0] + podniz_zamenjan


def pogovor():
    print("Zivjo. Kako ti je ime?")

    ime = input()

    print(f"Me veseli, {ime}. Koliko si star?")

    starost = int(input())

    print(f"Uffff, {starost} je veliko. Cez 5 let bos {starost + 5}")


def izpisi_zvezdice(n):
    if n == 0:
        return

    print(n * "*")

    izpisi_zvezdice(n - 1)


def izpisi_n_krat(niz, n):
    if n == 0:
        return

    print(niz)
    izpisi_n_krat(niz, n - 1)


def narisi_kvadrat(n):
    print(n * "*")  # zgornja stranica

    izpisi_n_krat("*" + (n - 2) * " " + "*", n - 2)

    print(n * "*")  # spodnja stranica
