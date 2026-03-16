def narisi_zvezdice(n):
    stevec = 1
    while stevec <= n:
        print(stevec * "*")
        stevec += 1


def stevilo_clenov_da_harmonicna_vrsta_preseze(x):
    vsota = 0
    n = 1

    while vsota <= x:
        vsota += 1 / n
        n += 1

    return n - 1


def stevilo_samoglasnikov(niz):
    stevilo = 0
    for crka in niz:
        if crka.lower() in "aeiou":
            stevilo += 1

    return stevilo


def zvezdice2(n):
    for i in range(1, n + 1):
        if i > 10:
            break

        if i == 3:
            continue

        print(i * "*")


def stejem_nazaj(n):
    for i in range(n, 0, -1):
        print(i)


def fakulteta(n):
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i

    return produkt


def je_podniz(podniz, niz):
    for i in range(len(niz) - len(podniz) + 1):
        sta_enaki = True
        for j in range(len(podniz)):
            if niz[i + j] != podniz[j]:
                sta_enaki = False
                break
        if sta_enaki:
            return True

    return False
