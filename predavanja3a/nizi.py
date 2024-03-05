def srednja_crka(niz):
    """Vrne srednjo crko niza."""
    indeks = len(niz) // 2
    crka = niz[indeks]

    return crka


def je_samoglasnik(crka):
    """Vrne True, ce je crka samoglasnik,
    sicer False."""

    if crka == "a" or crka == "e" or crka == "i" or crka == "o" or crka == "u":
        return True
    else:
        return False


def je_samoglasnik_bolje(crka):
    return crka in "aeiouAEIOU"


def prestej_samoglasnike(niz):
    """Vrne stevilo samoglasnikov
    v nizu."""
    if len(niz) == 0:
        return 0

    podniz = niz[0 : len(niz) - 1]
    samoglasnikov_v_podnizu = prestej_samoglasnike(podniz)

    if je_samoglasnik_bolje(niz[-1]):
        return samoglasnikov_v_podnizu + 1
    else:
        return samoglasnikov_v_podnizu


def pogovor():
    print("Zivijo, kako ti je ime?")
    ime = input()
    print(f"Hej {ime}. Lepo te je bilo spoznati. Koliko si star?")
    starost = int(input())
    print(f"cez pet let bos {starost + 5}")


def izpisi_zvezdice(n):
    if n == 0:
        return None

    print(n * "*")
    izpisi_zvezdice(n - 1)


def izpisi_zvezdice_interaktivno():
    print("koliko vrstic zvezdic naj izpisem:")
    n = int(input())

    izpisi_zvezdice(n)


def narisi_podpravokotnik(n, m):
    if n == 0:
        return

    print("|" + ((m - 2) * " ") + "|")
    narisi_podpravokotnik(n - 1, m)


def narisi_kvadrat(n):
    print(" " + ((n - 2) * "-") + " ")

    narisi_podpravokotnik(n, n)

    print(" " + ((n - 2) * "-") + " ")
