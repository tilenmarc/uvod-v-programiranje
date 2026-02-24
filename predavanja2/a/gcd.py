def gcd(n, m):
    """Vrne najvecji skupni delitelj n in m."""
    if m > n:
        m, n = n, m

    if n % m == 0:
        return m

    ostanek = n % m

    return gcd(m, ostanek)
