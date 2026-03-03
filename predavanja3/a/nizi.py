def srednje_znake(niz):
    stevilo_znakov = len(niz)
    sredina = stevilo_znakov // 2

    if niz == "":
        return ""
    elif stevilo_znakov % 2 == 1:
        return niz[sredina]
    else:
        return niz[sredina - 1 : sredina + 1]


def je_samoglasnik(crka):
    if crka in "aeiouAEIOU":
        return True
    else:
        return False


def stevilo_samoglasnikov(niz):
    """Vrne stevilo samoglasnikov v nizu."""
    if niz == "":
        return 0

    stevilo = 0
    if je_samoglasnik(niz[0]):
        stevilo += 1

    stevilo += stevilo_samoglasnikov(niz[1:])

    return stevilo


def pogovor():
    print("Zivjo, kako ti je ime?")

    ime = input()

    print(f"{ime} je lepo ime, koliko si star")

    starost = int(input())

    if starost > 50:
        print(f"uff res si star, cez 5 let bos {starost + 5}")
    else:
        print("super zate")

    print("kaj rad jes?")

    input()
    kajse()


def kajse():
    print("kaj se?")
    input()

    kajse()


def narisi_zvezdice(n):
    if n == 0:
        return

    print(n * "*")
    narisi_zvezdice(n - 1)


def narisi_zvezdice2(n, m):
    if n == 0:
        return

    presledkov = m - (2 * n - 1)
    print((presledkov // 2) * " " + (2 * n - 1) * "*" + (presledkov // 2) * " ")
    narisi_zvezdice2(n - 1, m)


def narisi_kvadrat(n):
    print(n * "*")

    izpisi_n_krat("*" + (n - 2) * " " + "*", n - 2)

    print(n * "*")


def izpisi_n_krat(niz, n):
    if n == 0:
        return

    print(niz)
    izpisi_n_krat(niz, n - 1)


def narisi_kvadrat2(n):
    print(n * "*")

    print((n - 2) * ("*" + (n - 2) * " " + "*\n"), end="")

    print(n * "*")
