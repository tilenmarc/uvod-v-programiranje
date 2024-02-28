def prva_rekurzija():
    print(111111111)

    prva_rekurzija()


def izpisi_stevila(n):
    """Funkcija izpise prvih n stevil
    padajoce."""

    print(n)
    if n == 0:
        return None
    else:
        izpisi_stevila(n - 1)

    return None


def fakulteta(n):
    """Funkcija vrne n * (n - 1) * ... * 1,
    kjer je n naravno stevilo."""
    if n == 1:
        return 1

    return n * fakulteta(n - 1)


def gcd(m, n):
    """Funkcija vrne najvecji skupni delitelj
    m in n."""
    if m < n:
        m, n = n, m

    ostanek = m % n

    if ostanek == 0:
        return n
    else:
        return gcd(n, ostanek)


def gcd2(m, n):
    return n if m % n == 0 else gcd(n, m % n)
