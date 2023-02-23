def rekurzivna_funkcija(x):
    """To je prvi primer rekurzivne funkcije."""
    if x == 0:
        return None

    print(x)
    rekurzivna_funkcija(x - 1)


def fakulteta(x):
    """Vrne n * (n - 1) * ... * 1
    kjer predpostavljam, da je x naravno
    stevilo."""
    if x == 0:
        return 1

    return x * fakulteta(x - 1)


def gcd(m, n):
    """Vrne najvecji skupni delitelj m in n."""
    if n > m:
        return gcd(n, m)

    r = m % n
    if r == 0:
        return n

    return gcd(n, r)


# Ta verzija gcd demostrira uporabo pogojnega
# izraza. Deluje samo ce m > n.
def gcd(m, n):
    return n if m % n == 0 else gcd(n, m % n)


def fibonacci(n):
    """Vrne n-ti clen Fibonaccijevega zaporedja.
    Zal je funkcija pocasna."""
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def posploseni_fibonacci(n, a=0, b=1):
    """Vrne n-ti clen posplosenega Fibonaccijevega
    zaporedja. Deluje hitro."""
    if n == 0:
        return a
    elif n == 1:
        return b

    return posploseni_fibonacci(n - 1, b, a + b)
