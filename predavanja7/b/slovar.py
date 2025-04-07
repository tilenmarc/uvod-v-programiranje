class Slovar:
    def __init__(self, pari, n=0):
        if n == 0:
            n = len(pari)
        self.dolzina = len(pari)
        self.predali = [[] for _ in range(n)]
        for par in pari:
            self[par[0]] = par[1]

    def __setitem__(self, kljuc, vrednost):
        if kljuc in self:
            del self[kljuc]

        self.predali[hash(kljuc) % len(self.predali)].append((kljuc, vrednost))
        self.dolzina += 1

    def __getitem__(self, kljuc):
        predal = self.predali[hash(kljuc) % len(self.predali)]
        for par in predal:
            if kljuc == par[0]:
                return par[1]

        return None

    def __contains__(self, kljuc):
        predal = self.predali[hash(kljuc) % len(self.predali)]
        for par in predal:
            if kljuc == par[0]:
                return True

        return False

    def __delitem__(self, kljuc):
        predal = self.predali[hash(kljuc) % len(self.predali)]
        for i in range(len(predal)):
            if kljuc == predal[i][0]:
                del predal[i]
                self.dolzina -= 1
                return

    def __len__(self):
        return self.dolzina


import random

nakljucni_pari = [
    (f"kljuc {random.randint(0, 1000)}", f"vrednost {random.randint(0, 1000)}")
    for _ in range(500)
]

import stopaj

stopaj.izmeri_case_poskusov(
    [
        [
            (f"kljuc {random.randint(0, n)}", f"vrednost {random.randint(0, n)}")
            for _ in range(n * 1000)
        ]
        for n in range(1, 20)
    ],
    [
        lambda pari: Slovar(pari, len(pari)),
    ],
)

stopaj.izmeri_case_poskusov(
    [
        Slovar(
            [
                (
                    f"kljuc {random.randint(0, n * 1000)}",
                    f"vrednost {random.randint(0, n * 1000)}",
                )
                for _ in range(n * 1000)
            ]
        )
        for n in range(1, 20)
    ],
    [
        lambda slovar: 0 in slovar,
    ],
)
