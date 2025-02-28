def fakulteta(n):
    """Izracuna n * (n - 1) * ... * 1."""
    if n == 1:
        return 1

    rezultat = n * fakulteta(n - 1)

    return rezultat


def vsota_kvadratov(n):
    if n == 1:
        return 1

    return n**2 + vsota_kvadratov(n - 1)


def gcd(n, m):
    """Izracuna najvecji skupni delitelj
    m in in n s pomocjo Evklidovega algoritma."""
    if n < m:
        m, n = n, m

    ostanek = n % m
    if ostanek == 0:
        return m

    return gcd(m, ostanek)


def gcd_kratko(n, m):
    return m if n % m == 0 else gcd_kratko(m, n % m)
