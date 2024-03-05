def izpisi_trikrat(f, x):
    print(f(x))
    print(f(x))
    print(f(x))


def predznak(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def nicle_funkcije(f, a, b, epsilon=10 ** (-10)):
    """Funkcija naj vrne niclo funkcije f
    na intervalu [a, b], kjer predpostavljamo,
    da predznak(f(a)) != predznak(f(b))"""

    if b - a < epsilon:
        return (a + b) / 2

    levo_krajisce = f(a)
    sredisce = f((a + b) / 2)
    if sredisce == 0:
        return (a + b) / 2

    if predznak(sredisce) != predznak(levo_krajisce):
        return nicle_funkcije(f, a, (a + b) / 2, epsilon)
    else:
        return nicle_funkcije(f, (a + b) / 2, b, epsilon)


def neki_polinom(x):
    return x**3 + 3 * x**2 + 8


def narisi_vrstico(f, x1, x2, y2, n):
    if n == 0:
        print()
        return

    if abs(f(x1, y2)) < 10 ** (-1):
        print("*", end="")
    else:
        print(" ", end="")

    narisi_vrstico(f, x1 + (x2 - x1) / n, x2, y2, n - 1)


def implicitna_funkcija(f, x1, x2, y1, y2, n, m):
    """Narise naj nicle funkcije f na intervalu
    [x1, x2] x [y1, y2]."""
    if n == 0:
        return

    narisi_vrstico(f, x1, x2, y2, m)

    implicitna_funkcija(f, x1, x2, y1, y2 - (y2 - y1) / n, n - 1, m)


def f(x, y):
    return x**2 + y**2 - 1
