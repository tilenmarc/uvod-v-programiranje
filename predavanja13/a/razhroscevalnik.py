def gcd(n, m):
    """Vrne najvecji skupni delitelj
    izracunan s pomocjo Evklidovega
    algoritma."""
    if m > n:
        n, m = m, n
    ostanek = n % m

    if ostanek == 0:
        return m

    nov_n = m
    nov_m = ostanek

    rezultat = gcd(nov_n, nov_m)

    return rezultat


x = 500
y = 158

print(gcd(x, y))
