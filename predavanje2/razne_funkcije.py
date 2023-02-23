def funkcija_z_dvema_returnoma(x):
    return x**2
    return x**3


def funkcija_brez_returna(x):
    a = x**3
    print(a)
    print(a + 2)


def funkcija_z_definiranimi_parametri(x, y=10, z=15):
    return x + y + z


y = 10
x = 5


def funkcija_z_globalno_vrednostjo(x):
    """Funkcija, ki demostrira uporabo
    globalnih spremenjivk."""

    # sedaj bom vrnil kar eno vrednost
    # sedaj bom vrnil vrednost x + y
    return x + y  # to je zadnja vrstica


funkcija_z_globalno_vrednostjo(x)


# pet krat ***f asdf - sintakticna napaka

# a = c
# 2 * funkcija_brez_returna(3)


def kvadrat(x):
    a = x**3
    print(a)

    return a
