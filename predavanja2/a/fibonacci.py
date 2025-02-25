def fibonacci(n):
    """Vrne n-ti clen Fibonaccijevega
    zaporedja. Pocasna."""
    if n == 1 or n == 0:
        return 1

    rezultat = fibonacci(n - 2) + fibonacci(n - 1)

    return rezultat


def posploseni_fibonacci(n, a=1, b=1):
    """Vrne n-ti clen posplosenega
    Fibonaccijevega zaporedja s prvima
    clenoma a in b."""

    if n == 0:
        return a
    if n == 1:
        return b

    rezultat = posploseni_fibonacci(n - 1, b, a + b)

    return rezultat
