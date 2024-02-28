def fibonacci(n):
    """Funkcija vrne n-ti clen Fibonaccijevega
    zaporedja."""

    if n == 0 or n == 1:
        return 1

    x = fibonacci(n - 1)
    y = fibonacci(n - 2)

    return x + y


def fibonacci_hitreje(n, a=1, b=1):
    """Funckija vren n-ti clen Fibonaccijevega
    zaporedja, kjer je zahtevnost linearna v
    odvisnosti od n."""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_hitreje(n - 1, b, a + b)
