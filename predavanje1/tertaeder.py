def ploscina_trikotnika(x, y, z):
    s = (x + y + z) / 2
    ploscina_xyz = (s * (s - x) * (s - y) * (s - z)) ** (1 / 2)

    return ploscina_xyz


def ploscina_tetraedra(a, b, c, d, e, f):
    ploscina = ploscina_trikotnika(a, b, c)
    ploscina = ploscina + ploscina_trikotnika(a, d, e)
    ploscina = ploscina + ploscina_trikotnika(b, e, f)
    ploscina = ploscina + ploscina_trikotnika(c, d, f)

    return ploscina


rezultat = ploscina_tetraedra(1, 1, 1, 2, 2, 2)
