import stopaj


def poisci_v_neurejenem(sez, x):
    return x in sez


def naredi_neurejenega(elementi):
    sez = []
    for x in elementi:
        sez.append(x)


def ali_vsebuje_urejen_seznam(x, sez):
    zacetek = 0
    konec = len(sez)
    while True:
        if konec - zacetek == 1:
            return x == sez[zacetek]
        sredina = (zacetek + konec) // 2
        if sez[sredina] == x:
            return True
        elif sez[sredina] > x:
            konec = sredina
        else:
            zacetek = sredina + 1


def poisci_v_urejenem(sez, x, i=0, j=None):
    if j is None:
        j = len(sez)
    if i >= j:
        return i
    else:
        sredina = (i + j) // 2
        if x == sez[sredina]:
            return None
        elif x < sez[sredina]:
            return poisci_v_urejenem(sez, x, i, sredina)
        elif x > sez[sredina]:
            return poisci_v_urejenem(sez, x, sredina + 1, j)
        else:
            assert False


def naredi_urejenega(elementi):
    sez = []
    for x in elementi:
        i = poisci_v_urejenem(sez, x)
        if i is not None:
            sez.insert(i, x)


def poisci_v_mnozici(mn, x):
    return x in mn


def naredi_mnozico(elementi):
    mn = set()
    for x in elementi:
        mn.add(x)


stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_seznam(500 * n) for n in range(1, 50)],
    [
        lambda sez: poisci_v_neurejenem(sez, 0),
    ],
)
stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_narascajoc_seznam(500 * n) for n in range(1, 50)],
    [
        lambda sez: ali_vsebuje_urejen_seznam(0, sez),
    ],
)
stopaj.izmeri_case_poskusov(
    [set(stopaj.nakljucen_seznam(500 * n)) for n in range(1, 50)],
    [
        lambda sez: poisci_v_mnozici(sez, 0),
    ],
)


stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_seznam(500 * n) for n in range(1, 20)],
    [
        lambda sez: naredi_neurejenega(sez),
    ],
)
stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_seznam(500 * n) for n in range(1, 20)],
    [
        lambda sez: naredi_urejenega(sez),
    ],
)
stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_seznam(500 * n) for n in range(1, 20)],
    [
        lambda sez: naredi_mnozico(sez),
    ],
)
