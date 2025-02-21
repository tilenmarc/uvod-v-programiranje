# a = 1
# b = 1
# c = 1
# d = 1
# e = 1
# f = 1

# s_abc = (1 / 2) * (a + b + c)
# abc = (s_abc * (s_abc - a) * (s_abc - b) * (s_abc - c)) ** (1 / 2)


def ploscina_trikotnika(x, y, z):
    """Izracuna ploscino trikotnika iz dolzin
    njegovih stranic.."""

    # uporabim Heronovo formulo
    s = (1 / 2) * (x + y + z)
    ploscina = (s * (s - x) * (s - y) * (s - z)) ** (1 / 2)

    return ploscina


def povrsina_tetraedra(a, b, c, d, e, f):
    """Izracuna povrsino tertraedra iz dolzin
    njegovih stranic."""
    abc = ploscina_trikotnika(a, b, c)
    ade = ploscina_trikotnika(a, d, e)
    cdf = ploscina_trikotnika(c, d, f)
    bef = ploscina_trikotnika(b, e, f)

    povrsina = abc + ade + cdf + bef

    return povrsina
