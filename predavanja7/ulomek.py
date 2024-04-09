import math


class Ulomek:
    def __init__(self, stevec, imenovalec=1):
        assert imenovalec != 0

        self.stevec = stevec
        self.imenovalec = imenovalec
        self.pokrajsaj()

    def pokrajsaj(self):
        gcd = math.gcd(self.stevec, self.imenovalec)
        self.imenovalec = self.imenovalec // gcd
        self.stevec = self.stevec // gcd
        if self.imenovalec < 0:
            self.imenovalec = -self.imenovalec
            self.stevec = -self.stevec

    def __eq__(self, drugi):
        self.pokrajsaj()
        drugi.pokrajsaj()
        return self.stevec == drugi.stevec and self.imenovalec == drugi.imenovalec

    def __add__(self, drugi):
        imenovalec = self.imenovalec * drugi.imenovalec
        stevec = self.stevec * drugi.imenovalec + drugi.stevec * self.imenovalec

        return Ulomek(stevec, imenovalec)

    def __repr__(self):
        return f"{self.stevec} / {self.imenovalec}"
