class Ulomek:
    def __init__(self, stevec, imenovalec):
        self.im = imenovalec
        self.st = stevec
        self.pokrajsaj()

    def __add__(self, other):
        st = self.st * other.im + self.im * other.st
        im = self.im * other.im
        return Ulomek(st, im)

    def __mul__(self, other):
        return Ulomek(self.st * other.st, self.im * other.im)

    def __eq__(self, value):
        self.pokrajsaj()
        value.pokrajsaj()

        return self.im == value.im and self.st == value.st

    def pokrajsaj(self):
        d = gcd(self.im, self.st)

        if self.im < 0:
            self.im *= -1
            self.st *= -1

        self.st = self.st // d
        self.im = self.im // d

    def pokrajsaj2(self):
        nov = Ulomek(self.st, self.im)
        nov.pokrajsaj()

        return nov

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
