def srednja_crka(niz):
    """Vrne srednjo črko."""
    dolzina = len(niz)

    return niz[dolzina // 2]


def je_samoglasnik(niz):
    """Vrne True, če je niz samoglsnik."""
    if len(niz) != 1:
        return False
    elif niz in "aeiouAEIOU":
        return True
    else:
        return False


def je_samoglasnik(niz):
    """Vrne True, če je niz samoglsnik. Lepša verzija"""
    return len(niz) == 1 and niz in "aeiouAEIOU"


def stevilo_samoglasnikov(niz):
    """Vrne število samoglasnikov, ki se pojavijo
    v nizu."""
    if niz == "":
        return 0

    a = stevilo_samoglasnikov(niz[1 : len(niz)])
    b = int(je_samoglasnik(niz[0]))

    return a + b


def pogovor():
    """Funkcija demonstrira uporabo input funkcije."""
    print("Hej, kako ti je ime?")
    ime = input()
    print(f"Me veseli {ime}")


def zvezdice(n):
    if n == 0:
        return None
    print(n * "*")
    zvezdice(n - 1)


def zvezdice_vprasaj():
    print("Koliko zvezdic želis?")
    n = int(input())

    zvezdice(n)


def podkvadrat(n, m):
    if n == 0:
        return None
    print("|" + (m * " ") + "|")
    podkvadrat(n - 1, m)


def kvadrat(n):
    print(" " + (n * "-") + " ")
    podkvadrat(n, n)
    print(" " + (n * "-") + " ")
