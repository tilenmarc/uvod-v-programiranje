class Ulomek:
    def __init__(self, stevec, imenovalec):
        self.stevec = stevec
        self.imenovalec = imenovalec
        self.okrajsaj()

    def __add__(self, drugi_ulomek):
        return Ulomek(
            self.stevec * drugi_ulomek.imenovalec
            + drugi_ulomek.stevec * self.imenovalec,
            self.imenovalec * drugi_ulomek.imenovalec,
        )

    def __repr__(self):
        return f"Ulomek({self.stevec}, {self.imenovalec})"

    def okrajsaj(self):
        delitelj = gcd(self.imenovalec, self.stevec)
        self.stevec = self.stevec // delitelj
        self.imenovalec = self.imenovalec // delitelj
        if self.imenovalec < 0:
            self.imenovalec *= -1
            self.stevec *= -1

    def __mul__(self, drugi_ulomek):
        return Ulomek(
            self.stevec * drugi_ulomek.stevec, self.imenovalec * drugi_ulomek.imenovalec
        )

    def __equal__(self, drugi_ulomek):
        self.okrajsaj()
        drugi_ulomek.okrajsaj()

        return (
            self.imenovalec == drugi_ulomek.imenovalec
            and self.stevec == drugi_ulomek.stevec
        )


def gcd(n, m):
    return m if n % m == 0 else gcd(m, n % m)
