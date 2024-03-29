def praznam_mnozica(n=10):
    return [[] for _ in range(n)]


def dodaj_element(mnozica, element):
    indeks = element % len(mnozica)
    if element not in mnozica[indeks]:
        mnozica[indeks].append(element)


def ali_je_v_mnozici(mnozica, element):
    indeks = element % len(mnozica)
    return element in mnozica[indeks]
