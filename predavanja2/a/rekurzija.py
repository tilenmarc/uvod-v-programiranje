def prva_rekurzija():
    print(42)

    prva_rekurzija()


def stevila_padajoce(n):
    """Funkcija izpise prvih n stevil
    v padajocem vrstnem redu."""
    if n == 0:
        return
    else:
        print(n)
        stevila_padajoce(n - 1)


def fakulteta(n):
    """Izracuna n * (n - 1) * ... * 1."""
    if n == 1:
        return 1

    return n * fakulteta(n - 1)


def vsota_kvadratov(n):
    """Vrne 1 + 2**2 + 3**2 + ... + n**2."""
    if n == 1:
        return 1

    vsota = n**2 + vsota_kvadratov(n - 1)

    return vsota
