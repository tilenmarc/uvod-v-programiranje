zacetni_clen = 3
razlika = 5
zap = (zacetni_clen, razlika)


def n_ti_clen(zap, n):
    return zap[0] + n * zap[1]


class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni = zacetni_clen
        self.razlika = razlika

    def __getitem__(self, n):
        return self.zacetni + n * self.razlika

    def __add__(self, zap):
        return AritmeticnoZaporedje(
            self.zacetni + zap.zacetni, self.razlika + zap.razlika
        )

    def __repr__(self):
        return f"Zaporedje {self.zacetni}, {self.clen(1)}, {self.clen(2)},..."

    def vsota_clenov(self, n):
        """Vrne z_0 + z_1 + ... + z_(n-1)"""
        return (n / 2) * (self.clen(0) + self.clen(n - 1))

    def __mul__(self, other):
        pass

    def __contains__(self, item):
        return (item - self.zacetni) % self.razlika == 0

    def __eq__(self, zap):
        return self.zacetni == zap.zacetni and self.razlika == zap.razlika

    def __sub__(self, other):
        pass

    def __str__(self):
        return f"({self.zacetni}, {self.razlika})"

    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i += 1
