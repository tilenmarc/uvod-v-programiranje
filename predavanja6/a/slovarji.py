def prestej_znake(niz):
    """Funkcija preseteje stevilo pojavitev
    vsakega znaka v nizu."""
    pojavitve = {}

    for znak in niz:
        if znak not in pojavitve:
            pojavitve[znak] = 1
        else:
            pojavitve[znak] = pojavitve[znak] + 1

    return pojavitve


def prestej_znake2(niz):
    """Funkcija preseteje stevilo pojavitev
    vsakega znaka v nizu."""
    pojavitve = {}

    for znak in niz:
        pojavitve[znak] = pojavitve.get(znak, 0) + 1

    return pojavitve


def zanke_po_slovarju(slovar):
    for kljuc in slovar:
        print("kljuc", kljuc)

    for vrednost in slovar.values():
        print("vrednost", vrednost)

    for kljuc, vrednost in slovar.items():
        print("kljuc, vrednost", kljuc, vrednost)


def kljuc_najvecje_vrednosti(slovar):
    kljuc_najvecje = None
    najvecja = None
    for kljuc, vrednost in slovar.items():
        if kljuc_najvecje == None:
            kljuc_najvecje = kljuc
            najvecja = vrednost
        elif vrednost > najvecja:
            najvecja = vrednost
            kljuc_najvecje = kljuc

    return kljuc_najvecje


besedilo = """Odgovorni urednik revije Atlantic Jeffrey Goldberg je v ponedeljek razkril, da je bil sredi marca na povabilo domnevno svetovalca Bele hiše za nacionalno varnost Mika Waltza vključen v skupino na aplikaciji za sporočanje Signal, v kateri sta bila med člani tudi podpredsednik J. D. Vance in obrambni minister Pete Hegseth.

V skupini so bili med drugim tudi profili z imeni direktorja obveščevalne agencije Cia Johna Ratcliffa, direktorice nacionalne obveščevalne agencije Tulsi Gabbard in zunanjega ministra Marca Rubia.

Pri tem je imel Goldberg približno dve uri pred samim napadom na Jemen vpogled v zaupne vojaške načrte za napade na hutijevske upornike, vključno s paketi orožja, tarčami in časovnico. Kot kaže, je bil v skupino, ki je štela 18 članov, dodan pomotoma, je po poročanju BBC-ja dejal Goldberg.

Medtem ko je bil sprva skeptičen, ga je v resničnost podatkov prepričalo poročanje o napadih. Kmalu zatem je zapustil skupino, pri čemer ni nihče postavljal vprašanj glede njegove prisotnosti v njej.

"Če so že izbrali naključno telefonsko številko, vsaj ni šlo za nekoga, ki podpira hutijevce, saj so delili podatke, ki bi po mojem mnenju lahko ogrozili življenja ameriških vojakov, ki so bili vpleteni v to operacijo," je Goldberg dejal za ameriško javno televizijo PBS."""


matrika = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
matrika2 = {(1, 1): 1, (3, 2): 1}


def matrika_slovar_v_navavadna(matrika_slovar, n, m):
    matrika = [m * [0] for _ in range(n)]

    for kljuc in matrika_slovar:
        matrika[kljuc[0]][kljuc[1]] = matrika_slovar[kljuc]

    return matrika


def matrika_navadna_v_slovar(matrika_navadna):
    matrika_slovar = {}

    for i in range(len(matrika_navadna)):
        vrstica = matrika_navadna[i]
        for j in range(len(vrstica)):
            el = vrstica[j]
            if el != 0:
                matrika_slovar[(i, j)] = el

    return matrika_slovar, len(matrika_navadna), len(matrika_navadna[0])
