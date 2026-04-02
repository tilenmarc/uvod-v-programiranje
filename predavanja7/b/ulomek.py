class Ulomek:
    def __init__(self, stevec, imenovalec):
        self.st = stevec
        self.im = imenovalec
        self.pokrajsaj()

    def __add__(self, u):
        return Ulomek(self.im * u.st + self.st * u.im, self.im * u.im)

    def __mul__(self, u):
        return Ulomek(self.st * u.st, self.im * u.im)

    def __eq__(self, u):
        self.pokrajsaj()
        u.pokrajsaj()

        return self.im == u.im and self.st == u.st

    def pokrajsaj(self):
        d = gcd(self.im, self.st)
        self.st //= d
        self.im //= d

        if self.im < 0:
            self.im *= -1
            self.st *= -1

    def __repr__(self):
        return f"{self.st} / {self.im}"


def gcd(n, m):
    """Vrne najvecji skupni delitelj n in m."""
    if m > n:
        m, n = n, m

    if n % m == 0:
        return m

    ostanek = n % m

    return gcd(m, ostanek)
