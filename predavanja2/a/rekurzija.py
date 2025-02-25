def prva_rekurzija():
    print(111)

    prva_rekurzija()


def fakulteta(n):
    """Izracuna vrednost n * (n - 1) * ... * 1."""
    if n == 1:
        return 1

    return n * fakulteta(n - 1)


def izpisi_n_stevil_padajoce(n):
    print(n)

    if n == 1:
        return
    else:
        izpisi_n_stevil_padajoce(n - 1)


def fakulteta_med(n, m):
    """Vrne m * (m - 1) * ... * n."""
    if n == m:
        return m

    return m * fakulteta_med(n, m - 1)
