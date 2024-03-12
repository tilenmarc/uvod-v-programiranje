def je_samoglasnik(crka):
    return crka in "aeiouAEIOU"


def stevilo_samoglasnikov(niz):
    stevec = 0
    for crka in niz:
        if je_samoglasnik(crka):
            stevec += 1

    return stevec


def zamenjaj_samoglasnike_z_vprasaji(niz):
    """Funkcija vrne nov niz, v katerem so vsi
    samoglasniki zamenjani z vprasaji."""

    nov_niz = ""
    for crka in niz:
        if je_samoglasnik(crka):
            nov_niz = nov_niz + "?"
        else:
            nov_niz = nov_niz + crka
        # print(nov_niz)

    return nov_niz


def zanke(n):
    for i in range(n):
        if i == 10:
            continue
        if i == 20:
            break

        if i == 15:
            pass

        print(i)


def funkcija_ki_ni_se_napisana():
    pass


def narisi_kvadrat(n):
    print(" " + n * "-" + " ")

    stevec = 0
    while stevec < n:
        print("|" + n * " " + "|")
        stevec += 1

    # for stevec in range(n):
    #     print("|" + n * " " + "|")

    print(" " + n * "-" + " ")


def je_podniz(niz, podniz):
    """Vrne True, ce je podniz podniz
    niza, sicer vrne False."""

    for pozicija1 in range(len(niz)):
        najdeno = True
        for pozicija2 in range(len(podniz)):
            if not (niz[pozicija1 + pozicija2] == podniz[pozicija2]):
                najdeno = False
                break

        if najdeno:
            return True

    return False


def je_podniz2(niz, podniz):
    """Vrne True, ce je podniz podniz
    niza, sicer vrne False."""

    for pozicija in range(len(niz)):
        if podniz == niz[pozicija : pozicija + len(podniz)]:
            return True

    return False
