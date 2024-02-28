a = 5
b = 6
c = 7
d = 5
e = 5
f = 5


def ploscina_trikotnika(x, y, z):
    """Funkicja izpracuna ploscino trikotnika."""

    # uporabim Heronovo formulo
    s = (x + y + z) / 2
    ploscina = (s * (s - x) * (s - y) * (s - z)) ** (1 / 2)

    return ploscina


ploscina = ploscina_trikotnika(a, b, c)
print(ploscina)


def povrsina_tetraedra(x, y, z, q, w, e):
    povrsina1 = ploscina_trikotnika(x, y, z)
    povrsina2 = ploscina_trikotnika(x, q, w)
    povrsina3 = ploscina_trikotnika(y, w, e)
    povrsina4 = ploscina_trikotnika(z, q, e)

    povrsina = povrsina1 + povrsina2 + povrsina3 + povrsina4

    return povrsina


print(povrsina_tetraedra(a, b, c, d, e, f))
