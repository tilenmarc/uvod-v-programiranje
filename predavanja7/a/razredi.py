zacetni_clen = 3
razlika = 5


zaporedje = (zacetni_clen, razlika)


def vrni_n_ti_clen(zaporedje, n):
    zacetni_clen, razlika = zaporedje
    return zacetni_clen + n * razlika


class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def __getitem__(self, n):
        return self.zacetni_clen + n * self.razlika

    def __add__(self, drugo_zaporedje):
        return AritmeticnoZaporedje(
            self.zacetni_clen + drugo_zaporedje.zacetni_clen,
            self.razlika + drugo_zaporedje.razlika,
        )

    def __repr__(self):
        return f"zaporedje {self.zacetni_clen}, {self.vrni_n_ti_clen(1)}, {self.vrni_n_ti_clen(2)},..."

    def vsota_n_clenov(self, n):
        vsota = 0
        for i in range(0, n):
            vsota += self.vrni_n_ti_clen(i)

        return vsota

    def vsota_n_clenov_po_gaussu(self, n):
        return n * self.zacetni_clen + ((n * (n - 1)) / 2) * self.razlika

    def __str__(self):
        return f"AritmeticnoZaporedje({self.zacetni_clen}, {self.razlika})"

    def __eq__(self, drugo_zap):
        return (
            self.zacetni_clen == drugo_zap.zacetni_clen
            and self.razlika == drugo_zap.razlika
        )
