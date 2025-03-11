def je_samoglasnik(znak):
    return znak in "aeiouAEIOU"


def stevilo_samoglasnikov(niz):
    """Vrne stevilo samoglasnikov v
    nizu."""

    if niz == "":
        return 0

    if je_samoglasnik(niz[0]):
        return 1 + stevilo_samoglasnikov(niz[1:])
    else:
        return stevilo_samoglasnikov(niz[1:])


def zamenjaj_samoglasnike_z_vprasaji(niz):
    if niz == "":
        return niz

    if je_samoglasnik(niz[0]):
        return "?" + zamenjaj_samoglasnike_z_vprasaji(niz[1:])
    else:
        return niz[0] + zamenjaj_samoglasnike_z_vprasaji(niz[1:])
