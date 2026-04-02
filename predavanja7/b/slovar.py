pari = [("kljuc1", 6), ("kljuc2", 10)]


class Slovar:
    def __init__(self, pari, n=1000):
        self.predali = [[] for _ in range(n)]

        for kljuc, vrednost in pari:
            self[kljuc] = vrednost

    def __getitem__(self, kljuc):
        i = hash(kljuc) % len(self.predali)

        for k, v in self.predali[i]:
            if k == kljuc:
                return v

    def __setitem__(self, kljuc, vrednost):
        i = hash(kljuc) % len(self.predali)

        indeks = None
        for j in range(len(self.predali[i])):
            k = self.predali[i][j][0]
            if k == kljuc:
                indeks = j
                break
        if indeks != None:
            del self.predali[i][indeks]

        self.predali[i].append((kljuc, vrednost))

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        pass


import random

pari = [(random.randint(0, 1000), random.random()) for _ in range(1000)]
