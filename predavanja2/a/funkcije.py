import math

a = 10
b = 5


def blabla(a):
    """Globalni vs lokalni parametri."""
    print(a)
    print(b)


def predznak(x):
    if x > 0:
        return 1
    else:
        if x == 0:
            return 0
        else:
            return -1


def nicla_sinusa(a, b, epsilon=10 ** (-10)):
    """Poracuna niclo sinusa na intervalu [a, b],
    kjer sign(sina(a)) != sign(sin(b)) (obe ne 0)
    s pomocjo bisekcije."""

    sredisce = (a + b) / 2
    if b - a < epsilon:
        return sredisce

    sin_a = math.sin(a)
    # sin_b = math.sin(b)
    sin_sredisce = math.sin(sredisce)

    if predznak(sin_sredisce) == predznak(sin_a):
        return nicla_sinusa(sredisce, b, epsilon)
    elif predznak(sin_sredisce) == 0:
        return sredisce
    else:
        return nicla_sinusa(a, sredisce, epsilon)
