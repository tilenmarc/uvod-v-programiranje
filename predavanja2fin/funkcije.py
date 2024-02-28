def funkcija_z_dvema_returnoma():
    return 1
    return 0


def funkcija_brez_returna():
    x = 3 + 4


a = 3


def globalni_parametri(x):
    """Funkcija sesteje globalno in lokalno
    spremenljivko."""

    return a + x


x = 10


# to je komentar: ta funkcija primereja delovanje lokalnih in globalnih
# spremenljivk
def globalni_vs_lokalni(x):
    return x


def funkcija_z_neobveznimi_parametri(x, y=1, z=2):
    print(x, y, z)
