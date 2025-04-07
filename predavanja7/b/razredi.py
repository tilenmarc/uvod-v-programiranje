zacetni_clen = 4
razlika = 6
zaporedje = (zacetni_clen, razlika)


def n_ti_clen_zaporedja(zap, n):
    return zap[0] + n * zap[1]


class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def __getitem__(self, n):
        return self.zacetni_clen + n * self.razlika

    def __add__(self, drugo_zap):
        return AritmeticnoZaporedje(
            self.zacetni_clen + drugo_zap.zacetni_clen, self.razlika + drugo_zap.razlika
        )

    def __repr__(self):
        return f"zaporedje {self.zacetni_clen}, {self[1]}, {self[2]},..."

    def __contains__(self, x):
        preverba1 = (x - self.zacetni_clen) % self.razlika == 0
        preverba2 = (x - self.zacetni_clen) // self.razlika >= 0

        return preverba1 and preverba2

    def vsota_n_clenov(self, n):
        return n * self.zacetni_clen + ((n - 1) * n) / 2 * self.razlika

    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i += 1
