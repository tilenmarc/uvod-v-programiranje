# a = 1
# b = 1
# c = 1
# d = 2
# e = 2
# f = 2


def ploscina_trikotnika(a, b, c):
    """Izracuna ploscino trikotnika iz dolzin
    stranic."""

    # uporabim Heronovo formulo
    s = (1 / 2) * (a + b + c)
    ploscina = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)

    return ploscina


def povrsina_tetraedra(a, b, c, d, e, f):
    abc = ploscina_trikotnika(a, b, c)
    cef = ploscina_trikotnika(c, e, f)
    ebd = ploscina_trikotnika(e, b, d)
    fda = ploscina_trikotnika(f, d, a)

    povrsina = abc + cef + ebd + fda

    return povrsina
