def fakulteta(n):
    rezultat = 1
    for i in range(1, n + 1):
        rezultat *= i

    return rezultat


def je_samoglasnik(znak):
    """Vrne True, ce je znak samoglasnik, sicer False."""

    if znak in "aeiouAEIOU":
        return True
    else:
        return False


def stevilo_samoglasnikov(niz):
    stevec = 0

    for znak in niz:
        if je_samoglasnik(znak):
            stevec += 1

    return stevec


def zamenjaj_samoglasnike_z_vprasaji(niz):
    nov_niz = ""

    for znak in niz:
        if je_samoglasnik(znak):
            nov_niz = nov_niz + "?"
        else:
            nov_niz = nov_niz + znak

    return nov_niz


def narisi_kvadrat(n):
    print(n * "*")

    stevec = 0
    while stevec < n - 2:
        print("*" + (n - 2) * " " + "*")
        stevec += 1

    print(n * "*")


def for_with_break(n):
    for i in range(n):
        if i**2 > n:
            break

    return i


def for_with_continue(n):
    for i in range(n):
        if i % 2 == 0:
            continue

        print(i)


def funkcija(x, y, z):
    pass


def funkcija2():
    return 42


def je_podniz(niz, podniz):
    """Vrne True, ce podniz je v nizu,
    sicer false."""

    for indeks in range(len(niz) - len(podniz) + 1):
        so_enaki = True
        for indexs2 in range(len(podniz)):
            if niz[indeks + indexs2] != podniz[indexs2]:
                so_enaki = False
                break

        if so_enaki:
            return True

    return False
