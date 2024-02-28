def prva_rekurzija():
    print(11111111111)

    prva_rekurzija()


def izpisi_stevila(n):
    """Program izpise prvih n stevil padajoce."""

    print(n)

    if n == 0:
        # zelimo da se pri nicli ustavi
        return None
    else:
        # sicer problem prenesemo na manjsega
        izpisi_stevila(n - 1)


def fakulteta(n):
    """Funkcija vrne n * (n - 1) * ... * 1.
    Predpostavljamo, da je n naravno stevilo."""

    if n == 1:
        return 1

    rezultat = n * fakulteta(n - 1)

    return rezultat
