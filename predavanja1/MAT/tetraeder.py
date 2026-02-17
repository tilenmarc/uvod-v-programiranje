def povrsina_teraedra(x, y, z, w, u, v):
    trik1 = ploscina_trik(x, y, z)
    trik2 = ploscina_trik(y, v, w)
    trik3 = ploscina_trik(z, v, u)
    trik4 = ploscina_trik(x, w, u)

    return trik1 + trik2 + trik3 + trik4


def ploscina_trik(x, y, z):
    s = (x + y + z) / 2
    ploscina_xyz = (s * (s - x) * (s - y) * (s - z)) ** (1 / 2)

    return ploscina_xyz


a = 1
b = 1
c = 1
d = 2
e = 2
f = 2

print(povrsina_teraedra(a, b, c, d, e, f))
