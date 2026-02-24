ENKA = 1
b = 2


def funkcija1(x, b):
    y = b + ENKA

    return b + x


def uporabi_dvakrat(f, x):
    """Izracuna f(f(x))."""

    return f(f(x))
