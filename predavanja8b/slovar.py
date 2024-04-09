import stopaj
import random


class Slovar:
    def __init__(self, pari=[], n=1):
        if pari != [] and n == 1:
            n = len(pari)
        self.pari = [[] for _ in range(n)]
        self.length = 0
        for par in pari:
            self.__setitem__(par[0], par[1])

    def __setitem__(self, kljuc, vrednost):
        indeks = hash(kljuc) % len(self.pari)
        for i, par in enumerate(self.pari[indeks]):
            if par[0] == kljuc:
                del self.pari[indeks][i]
                self.length -= 1
                break
        self.pari[indeks].append((kljuc, vrednost))
        self.length += 1

    def __getitem__(self, kljuc):
        indeks = hash(kljuc) % len(self.pari)
        for par in self.pari[indeks]:
            if par[0] == kljuc:
                return par[1]
        return None

    def vec_predalckov(self, n):
        novi_predali = [[] for i in range(n)]
        for predal in self.pari:
            for par in predal:
                indeks = hash(par[0]) % n
                novi_predali[indeks].append(par)

        self.pari = novi_predali

    def __len__(self):
        return self.length


stopaj.izmeri_case_poskusov(
    [
        Slovar([(random.randint(0, 1000000), i * 10) for i in range(n * 500)])
        for n in range(1, 30)
    ],
    [
        lambda sez: sez[10],
    ],
)
