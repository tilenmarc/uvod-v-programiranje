def gcd(m, n):
    """Funkcija vrne najvecji skupni
    delitelj m in n."""
    if m < n:
        return gcd(n, m)

    ostanek = m % n
    if ostanek == 0:
        return n

    rezultat = gcd(n, ostanek)

    return rezultat


def gcd2(m, n):
    return n if m % n == 0 else gcd2(n, m % n)
