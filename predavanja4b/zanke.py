def prva_zanka(n):
    stevec = 0
    while stevec < n:
        print("UVP je najboljsi!", stevec)
        stevec += 1


def druga_zanka(n):
    for stevec in range(n):
        print("UVP je najboljsi!", stevec)


def tretja_zanka(niz):
    for crka in niz:
        print(f"Daj mi: {crka}")


def je_samoglasnik(crka):
    return crka in "aeiouAEIOU"


def zamenjaj_samoglasnike_z_vprasaji(niz):
    nov_niz = ""
    for crka in niz:
        if je_samoglasnik(crka):
            nov_niz = nov_niz + "?"
        else:
            nov_niz = nov_niz + crka

    return nov_niz


def stevilo_clenov_do(x):
    vsota = 0
    i = 1
    while vsota < x:
        vsota += 1 / i
        i += 1
        # print(i, vsota)

    return i - 1


def je_podniz(niz, podniz):
    for pozicija1 in range(len(niz) - len(podniz) + 1):
        preveri = True
        for pozicija2 in range(len(podniz)):
            if niz[pozicija1 + pozicija2] != podniz[pozicija2]:
                preveri = False
                break
        if preveri:
            return True

    return False
