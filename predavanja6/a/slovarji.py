def prestej_znake(niz):
    pojavitve = {}

    for znak in niz:
        if not znak.isalpha():
            continue
        znak = znak.lower()
        if znak not in pojavitve:
            pojavitve[znak] = 1
        else:
            pojavitve[znak] += 1

    return pojavitve


def zanke(slovar):
    for kljuc in slovar:
        print(kljuc)
    for vrednost in slovar.values():
        print(vrednost)
    for kljuc, vrednost in slovar.items():
        print(kljuc, vrednost)


def kljuc_najvecje_vrednosti(slovar):
    najvecja = None
    kljuc_najvecje = None
    for kljuc, vrednost in slovar.items():
        if najvecja == None or vrednost > najvecja:
            najvecja = vrednost
            kljuc_najvecje = kljuc

    return kljuc_najvecje


mat = [[1, 0, 0], [0, 0, 0], [1, 0, 0]]


def matrika_seznam_v_slovar(mat):
    mat_slovar = {}

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                continue

            mat_slovar[(i, j)] = mat[i][j]

    return (mat_slovar, len(mat), len(mat[0]))


def matrika_slovar_v_seznam(mat_slovar, n, m):
    matrika = []
    for _ in range(n):
        matrika.append(m * [0])

    for kljuc, vrednost in mat_slovar.items():
        i, j = kljuc

        matrika[i][j] = vrednost

    return matrika


niz = """
Parlamentarne volitve 2026 "Ob pirovi zmagi ni razloga za veselje"
Povolilni komentar Marinka Banjaca in Borisa Vezjaka

Pred pošiljko glasov po pošti in na diplomatskih predstavništvih Svoboda 7773 glasov pred SDS-om
Parlamentarne volitve 2026 Pred pošiljko glasov po pošti in na diplomatskih predstavništvih Svoboda 7773 glasov pred SDS-om
Izide glasovanja po pošti iz tujine in na diplomatskih predstavništvih bo DVK ugotavljal čez en teden

Božič Marolt: Volivci razmišljali taktično in se odločali med vodilnima oz. glasovali proti njima
Parlamentarne volitve 2026 Božič Marolt: Volivci razmišljali taktično in se odločali med vodilnima oz. glasovali proti njima
Največja "žrtev" taktičnega glasovanja Levica in Vesna, rezultat Demokratov ni presenečenje."""
