def sodi_iterator(n):
    i = 0
    while i < n:
        yield i
        i += 2


def prastevila():
    sez = []
    i = 2
    while True:
        je_prastevilo = True
        for j in sez:
            if i % j == 0:
                je_prastevilo = False
                break
        if je_prastevilo:
            yield i
            sez.append(i)
        i += 1
