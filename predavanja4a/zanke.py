def prva_zanka():
    while True:
        print("UVP je najboljsi")


def druga_zanka(n):
    pojavitve = 0
    while pojavitve < n:
        print(f"UVP je najboljsi v iteraciji {pojavitve}")
        pojavitve = pojavitve + 1


def zvezdice(n):
    stevec = 1
    while stevec <= n:
        print(stevec * "*")
        stevec += 1


def smrekica(n):
    stevec = 0
    while stevec < n:
        print((n - 1 - stevec) * " " + (2 * stevec + 1) * "*" + " " * (n - 1 - stevec))
        stevec += 1


def stevilo_clenov_v_harmonicni_vrsti_do(x):
    stevec = 0
    vsota = 0
    while vsota < x:
        vsota += 1 / (stevec + 1)
        stevec += 1
        # print(stevec, vsota)

    return stevec - 1


def prva_for_zanka(niz):
    for crka in niz:
        print(crka)


def for_range(n):
    for i in range(n):
        print(i)


def for_range2(n, m):
    for i in range(n, m):
        print(i)


def for_range3(n, m, j):
    for i in range(n, m, j):
        print(i)


def fakulteta(n):
    stevec = 1
    produkt = 1
    while stevec <= n:
        produkt *= stevec
        stevec += 1

    return produkt


def fakulteta2(n):
    produkt = 1

    for stevec in range(1, n + 1):
        produkt *= stevec

    return produkt
