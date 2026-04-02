def prestej_pojavitve(niz):
    pojavitve = {}

    for znak in niz:
        if znak not in pojavitve:
            pojavitve[znak] = 1
        else:
            pojavitve[znak] += 1

    return pojavitve


niz = """"Despre tine" (Romanian for 'About You') is a dance-pop song by the Moldovan band O-Zone, released as a single by Media Services in Romania around December 2002. Written and produced by the band's founder Dan Balan (pictured), it was included on a reissue of their second studio album Number 1 (2002) and later on their third studio album DiscO-Zone (2003). "Despre tine" was recorded in September 2002 at the MOF Records studio with the assistance of Bogdan Popoiag. Following the international success of O-Zone's 2003 single "Dragostea din tei", "Despre tine" was re-released in select European markets in August 2004. At the MTV Romania Music Awards 2003, "Despre tine" won Best Song and Best Dance. It also received a nomination for Best Dance-Pop Song at the Radio România Actualități Awards the same year. It topped the Romanian Top 100 in 2003 and reached number one in Norway in 2004. The song was certified double gold in Romania and gold in France."""


mat = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]


def matrika_seznam_v_slovar(mat):
    slovar = {}

    for i, vrstica in enumerate(mat):
        for j, el in enumerate(vrstica):
            if el != 0:
                slovar[(i, j)] = el

    return slovar, len(mat), len(mat[0])


def matrika_slovar_v_seznam(slovar, n, m):
    mat = [m * [0] for _ in range(n)]

    for kljuc, vrednost in slovar.items():
        i, j = kljuc
        mat[i][j] = vrednost

    return mat
