def fibonacci(n):
    """Vrne n-ti clen Fibonaccijevega zaporedja."""

    if n == 1 or n == 0:
        return 1

    prejsnji = fibonacci(n - 1)
    predprejsnji = fibonacci(n - 2)

    return prejsnji + predprejsnji


def posploseni_fibonacci(n, a=1, b=1):
    if n == 1:
        return b
    if n == 0:
        return a

    return posploseni_fibonacci(n - 1, b, a + b)
