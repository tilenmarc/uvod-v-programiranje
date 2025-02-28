def fibonacci(n):
    """Vrne n-ti clen Fibonaccijevega zaporedja."""
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def posploseni_fibonacci(n, a=1, b=1):
    """Vrne n-ti clen posplosenega
    Fibonaccijevega zaporedja s prvima
    clenoma a in b."""
    if n == 0:
        return a
    if n == 1:
        return b

    return posploseni_fibonacci(n - 1, b, a + b)
