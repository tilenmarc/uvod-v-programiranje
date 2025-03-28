def ustvari_prazno(n=10):
    return [[] for _ in range(n)]


def dodaj_v_mnozico(mnozica, x):
    stevilo_predalckov = len(mnozica)
    if x not in mnozica[x % stevilo_predalckov]:
        mnozica[x % stevilo_predalckov].append(x)


def je_v_mnozici(mnozica, x):
    stevilo_predalckov = len(mnozica)
    return x not in mnozica[x % stevilo_predalckov]
