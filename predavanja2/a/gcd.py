def gcd(n, m):
    """Vrne najvecji skupni delitelj
    izracunan s pomocjo Evklidovega
    algoritma."""
    if m > n:
        n, m = m, n
    print(n, m)
    ostanek = n % m

    if ostanek == 0:
        return m

    nov_n = m
    nov_m = ostanek

    rezultat = gcd(nov_n, nov_m)

    return rezultat


def gcd2(n, m):
    return m if n % m == 0 else gcd2(m, n % m)
