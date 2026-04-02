def iterator_sodi(n):
    i = 0
    while i < n:
        yield i
        i += 2


def vsi_nizi01(n):
    niz = n * "0"
    yield niz

    enke = n * "1"
    while niz != enke:
        for i in range(n):
            if niz[i] == "0":
                niz = i * "0" + "1" + niz[i + 1 :]
                yield niz
                break


def prastevila():
    pra = []

    i = 2
    while True:
        je_pra = True
        for j in pra:
            if i % j == 0:
                je_pra = False
                break
        if je_pra:
            pra.append(i)
            yield i

        i += 1
