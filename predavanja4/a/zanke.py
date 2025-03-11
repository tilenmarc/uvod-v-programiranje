def prva_zanka():
    while True:
        print("UVP je najboljsi")


def druga_zanka(n):
    stevec = 0

    while stevec < n:
        print(f"UVP je najboljsi, v iteraciji {stevec}")
        stevec = stevec + 1

    return None


def zvezdice(n):
    while n > 0:
        print(n * "*")
        n = n - 1


def zvezdice_obrnjeno(n):
    stevec = 1
    while stevec <= n:
        print(stevec * "*")
        stevec += 1


def stevilo_clenov_v_harmonicni_vrsti(x):
    """Funkcija izracuna stevilo clenov, da
    harmonicna vrsta preseze x."""

    vsota = 0
    i = 1
    while vsota < x:
        print(i, vsota)
        vsota += 1 / i
        i += 1

    return i - 1


def prva_for_zanka(niz):
    for znak in niz:
        print(znak)


def druga_for_zanka(crke):
    for crka in crke:
        print(f"Daj mi: {crka}")

    print(f"Gremo {crke}")


def for_range(n):
    for stevec in range(n):
        print(f"stejem {stevec}")


def for_range2(n):
    for stevec in range(1, n + 1):
        print(f"stejem {stevec}")


def for_range3(n):
    for stevec in range(0, 2 * n, 2):
        print(f"stejem soda stevila {stevec}")


def stejem_nazaj(n):
    while n > 0:
        print(n)
        n -= 1


def stejem_nazaj_for(n):
    for stevec in range(n, 0, -1):
        print(stevec)
