def zanka_while():
    i = 0
    while i < 10:
        print("Hello!", i)
        i += 1


def zanka_for(niz):
    for crka in niz:
        print(crka)


def zanka_for_range(n):
    for i in range(n, -5, -1):
        print(i)


def fakulteta(n):
    x = 1
    for i in range(2, n + 1):
        x *= i

    return x


def zamenjaj_samoglasnike_z_vprasaji(niz):
    koncen_niz = ""
    for crka in niz:
        if crka in "aeiouAEIOU":
            koncen_niz += "?"
        else:
            koncen_niz += crka

    return koncen_niz
