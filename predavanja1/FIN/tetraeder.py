def ploscina_trikotnika(x, y, z):
    s = (x + y + z) / 2
    ploscina_abc = (s * (s - x) * (s - y) * (s - z)) ** (1 / 2)

    return ploscina_abc


def ploscina_tetraedra(x, y, z, w, u, v):
    trik1 = ploscina_trikotnika(x, y, z)
    trik2 = ploscina_trikotnika(x, w, v)
    trik3 = ploscina_trikotnika(y, u, v)
    trik4 = ploscina_trikotnika(z, w, u)

    return trik1 + trik2 + trik3 + trik4


a = 1
b = 1
c = 1
d = 2
e = 2
f = 2

print(ploscina_tetraedra(a, b, c, d, e, f))
