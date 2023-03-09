def prva_zanka():
    while True:
        print("UVP je najboljsi!")


def druga_zanka(n):
    i = 0
    while i < n:
        print("UVP je najboljsi!", i)
        i = i + 1


def zvezdice(n):
    i = 1
    while i <= n:
        print(i * "*")
        i = i + 1


def zvezdice2(n):
    znaki = "*"
    while len(znaki) <= n:
        print(znaki)
        znaki = znaki + "*"


def stevilo_clenov_da_preseze(x):
    """Vrne stevilo clenov geometrijske vrste,
    da njihova vsota preseze vrednost x."""
    vsota = 0
    i = 0
    while vsota <= x:
        i += 1
        vsota = vsota + (1 / i)

    return i


def prva_zanka_for(niz):
    for crka in niz:
        print(crka)


def druga_zanka_for_range(n):
    for i in range(n + 1, 1, -2):
        print(i * "*")


def zanka_z_nizom_in_range(niz):
    for i in range(len(niz)):
        print(f"Daj mi {niz[i]}", i)
