def funkcija_s_komentarji(x):
    """To je primer funkcije, ki ima dokumentacijo."""

    # tu uporabimo Eulerjevo formulo
    x = x**2

    x = x + 1

    return x


KOREN2 = 2 ** (1 / 2)
x = 2


def funkcija_z_globalnimi_spremenljivkami(x):
    x = x + KOREN2

    def blabla():
        print("blabla")

    blabla()

    return x


def funkcija_s_parametri(x, y=1, z=2):
    print(x, y, z)
