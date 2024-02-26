a = 2
b = 4
print(a + b)

a = 10
b = 11
c = 5


def ploscina_trikotnika(x, y, z):
    s = (x + y + z) / 2
    ploscina = (s * (s - x) * (s - y) * (s - z)) ** (1 / 2)

    return ploscina


print(ploscina_trikotnika(a, b, c))


def povrsina_tetraedra(x, y, z, w, q, e):
    trikotnik1 = ploscina_trikotnika(x, y, z)
    trikotnik2 = ploscina_trikotnika(x, w, q)
    trikotnik3 = ploscina_trikotnika(y, q, e)
    trikotnik4 = ploscina_trikotnika(z, w, e)

    povrsina = trikotnik1 + trikotnik2 + trikotnik3 + trikotnik4

    return povrsina


d = 10
e = 10
f = 10

print(povrsina_tetraedra(a, b, c, d, e, f))
