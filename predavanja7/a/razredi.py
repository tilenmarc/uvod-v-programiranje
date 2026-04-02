def n_ti_clen(a, b, n):
    """Racuna n-ti clen aritmeticnega
    predstavljeno z a zacetni clen in b
    razlika.
    """
    return a + n * b


class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def __getitem__(self, n):
        return self.zacetni_clen + n * self.razlika

    def vsota(self, n):
        "Vrne z_0 + z_1 + ... + z_n"
        return (n + 1) * self.zacetni_clen + (n * (n + 1) // 2) * self.razlika

    def __add__(self, drugo_zap):
        return AritmeticnoZaporedje(
            self.zacetni_clen + drugo_zap.zacetni_clen, self.razlika + drugo_zap.razlika
        )

    def __repr__(self):
        return f"Zaporedje: {self.zacetni_clen}, {self.zacetni_clen + self.razlika},..."

    def __contains__(self, clen):
        ostanek = (clen - self.zacetni_clen) % self.razlika
        delitelj = (clen - self.zacetni_clen) // self.razlika

        return ostanek == 0 and delitelj >= 0

    def __mul__(self, other):
        pass

    def __str__(self):
        return f"({self.zacetni_clen}, {self.razlika})"

    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i += 1
