vrednost = 10
a = 5


def uporaba_globalne(x, a):
    """Funkcija demonstrira uporabo
    lokalnih in globalnih spremenljivk."""
    return vrednost + x + a


def uporabi_veckrat(x, funkcija_ki_jo_uporabim, n):
    if n == 0:
        return x

    return funkcija_ki_jo_uporabim(uporabi_veckrat(x, funkcija_ki_jo_uporabim, n - 1))


def nicla_funkcije(f, a, b, epsilon=10 ** (-10)):
    """Vrne x, za kateri je f(x) == 0, kjer predpostavljamo,
    da f(a) * f(b) < 0."""
    sredina = (a + b) / 2
    if b - a < epsilon:
        return sredina

    if f(sredina) == 0:
        return sredina
    elif f(a) * f(sredina) < 0:
        return nicla_funkcije(f, a, sredina, epsilon)
    else:
        return nicla_funkcije(f, sredina, b, epsilon)


def polinom(x):
    return 10 * x**3 + x - 4


def ploscina_stolpca(x, y):
    return x * y


def doloceni_integral(f, a, b, n):
    """Izracuna doloceni integral f(x) med
    a in b, s pomocjo Riemannove vsote, kjer
    interval razdeli na n delov."""
    if n == 1:
        return ploscina_stolpca((b - a), f(b))

    nov_b = b - ((b - a) / n)

    return doloceni_integral(f, a, nov_b, n - 1) + ploscina_stolpca(
        (b - a) / n, f(nov_b)
    )


def doloceni_integral2(f, a, b, n):
    """Izracuna doloceni integral f(x) med
    a in b, s pomocjo rimanove vsote, kjer
    interval razdeli na 2**n delov."""
    if n == 1:
        return ploscina_stolpca((b - a), f(b))

    sredina = (a + b) / 2

    return doloceni_integral2(f, a, sredina, n - 1) + doloceni_integral2(
        f, sredina, b, n - 1
    )
