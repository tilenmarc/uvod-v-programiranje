def naredi_prazno_mnozico(n=100):
    return [[] for _ in range(n)]


def dodaj_v_mnozico(mn, x):
    stevilo_predalckov = len(mn)
    pozicija = hash(x) % stevilo_predalckov

    if x not in mn[pozicija]:
        mn[pozicija].append(x)


def ali_vsebuje(mn, x):
    stevilo_predalckov = len(mn)
    pozicija = hash(x) % stevilo_predalckov

    return x in mn[pozicija]


import random

n = 100000

mn = naredi_prazno_mnozico(n)

for _ in range(n):
    dodaj_v_mnozico(mn, random.randint(0, n * 1000))
