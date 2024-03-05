def je_samoglasnik(crka):
    return crka in "aeiouAEIOU"


def stevilo_samoglasnikov(niz):
    if len(niz) == 0:
        return 0

    stevec = 0
    if je_samoglasnik(niz[0]):
        stevec += 1

    stevec += stevilo_samoglasnikov(niz[1 : len(niz)])

    return stevec


def zamenjaj_samoglasnike_z_vprasaji(niz):
    if len(niz) == 0:
        return niz

    if je_samoglasnik(niz[0]):
        crka = "?"
    else:
        crka = niz[0]

    nov_niz = crka + zamenjaj_samoglasnike_z_vprasaji(niz[1:])

    return nov_niz


def pogovor():
    print("Zivijo, kako ti je ime?")
    ime = input()
    print(f"Me veseli {ime}. Koliko si star?")
    starost = input()
    print(f"uff, {starost} je precej, moram iti.")


def izpisi_rob(n, m):
    if n == 0:
        return

    print("|" + ((m - 2) * " ") + "|")
    izpisi_rob(n - 1, m)


def izpisi_kvadrat(n):
    print(" " + ((n - 2) * "-") + " ")

    izpisi_rob(n - 2, n)

    print(" " + ((n - 2) * "-") + " ")
