class Slovar:
    def __init__(self):
        self.pari = []

    def vstavi(self, kljuc, vrednost):
        self.pari.append((kljuc, vrednost))

    def __getitem__(self, kljuc):
        for par in self.pari:
            if par[0] == kljuc:
                return par[1]
