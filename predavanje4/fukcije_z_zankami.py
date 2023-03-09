def fakulteta(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


def stevilo_samoglasnikov(niz):
    stevec = 0
    for crka in niz:
        if crka in "aeiouAEIOU":
            stevec += 1

    return stevec


def zamenjaj_samoglasnike_z_vprasaji(niz):
    """Vrne nov niz, kjer so vsi samoglasniki
    zamenjani z vprasaji."""
    koncen_niz = ""
    for crka in niz:
        if crka in "aeiouAEIOU":
            koncen_niz += "?"
        else:
            koncen_niz += crka

    return koncen_niz


def narisi_kvadrat(n):
    print(" " + n * "-" + " ")
    for _ in range(n):
        print("|" + n * " " + "|")
    print(" " + n * "-" + " ")


import math


def nicla_sinusa(a, b, eps):
    """Vrne vrednost x, da je sin(x) = 0 in
    a <= x <= b, kjer je 0 != sign(sin(a)) != sign(sin(b))."""
    while abs(b - a) > eps:
        # print(a, b)
        sredina = (a + b) / 2
        sin_sredina = math.sin(sredina)
        if sin_sredina == 0:
            return sredina
        sin_a = math.sin(a)
        if sin_sredina * sin_a > 0:
            a = sredina
        else:
            b = sredina
    return (a + b) / 2
