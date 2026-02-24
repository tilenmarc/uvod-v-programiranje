def primer_rekurzije():
    print(42)

    primer_rekurzije()


def fakulteta(n):
    """Funkcija vrne n * (n - 1) * ... * 1.
    n mora biti tipa int in vsaj 1."""
    if n <= 1:
        return 1

    return n * fakulteta(n - 1)


def gcd(n, m):
    if m > n:
        n, m = m, n

    ostanek = n % m
    if ostanek == 0:
        return m

    return gcd(m, ostanek)


def gcd2(n, m):
    return gcd2(m, n % m) if n % m != 0 else m


def nicla(f, a, b, epsilon):
    """Poisce niclo zvezne funkcije f,
    kjer 0 != sign(f(a)) != sign(f(b))."""

    if abs(b - a) < epsilon:
        return (a + b) / 2

    if f((a + b) / 2) == 0:
        return (a + b) / 2
    elif f((a + b) / 2) * f(a) > 0:
        return nicla(f, (a + b) / 2, b, epsilon)
    else:
        return nicla(f, a, (a + b) / 2, epsilon)


def polinom(x):
    return x * (x - 4) * (x - 9)


def integriraj(f, a, b, n):
    if n == 0:
        return 0

    sirina_stolpca = (b - a) / n
    stolpec = sirina_stolpca * f((a + sirina_stolpca / 2))

    return stolpec + integriraj(f, a + sirina_stolpca, b, n - 1)


def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def posploseni_fibonacci(n, a=1, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return posploseni_fibonacci(n - 1, b, a + b)
