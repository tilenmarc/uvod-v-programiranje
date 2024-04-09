zacetni = 5
razlika = 10
zaporedje = (zacetni, razlika)


def n_ti_element(zap, n):
    """Vrne n-ti element, kjer je zap podano
    kot par (zacenti_clen, razlika)."""
    zacetni_el = zap[0]
    razlika_el = zap[1]

    return zacetni_el + n * razlika_el


class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def n_ti_clen(self, n):
        """Glej tudi spodaj funkcijo __getitem__"""
        return self.zacetni_clen + n * self.razlika

    def vsota_n_clenov(self, n):
        vsota = 0
        for i in range(n):
            vsota += self.n_ti_clen(i)

        return vsota

    def vsota_n_clenov_gauss(self, n):
        return self.zacetni_clen * n + self.razlika * (n * (n - 1) / 2)

    def __add__(self, drugo_zaporedje):
        zacetni = self.zacetni_clen + drugo_zaporedje.zacetni_clen
        razlika = self.razlika + drugo_zaporedje.razlika

        return AritmeticnoZaporedje(zacetni, razlika)

    def __repr__(self):
        return f"Zaporedje({self.zacetni_clen}, {self.razlika})"

    def __str__(self):
        return f"Zaporedje({self.zacetni_clen}, {self.razlika})"

    def __eq__(self, drugo_zap):
        return (
            self.zacetni_clen == drugo_zap.zacetni_clen
            and self.razlika == drugo_zap.razlika
        )

    def __contains__(self, x):
        return (x - self.zacetni_clen) % self.razlika == 0

    def __getitem__(self, n):
        return self.zacetni_clen + n * self.razlika

    def __iter__(self):
        clen = self.zacetni_clen
        while True:
            yield clen
            clen += self.razlika


def moj_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


def moj_range_slabse(n):
    return [i for i in range(n)]
