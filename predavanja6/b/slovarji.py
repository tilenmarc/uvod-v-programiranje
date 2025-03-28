def zanke_po_slovarju(slovar):
    for kljuc in slovar:
        print(kljuc)

    for vrednost in slovar.values():
        print(vrednost)

    for kljuc, vrednost in slovar.items():
        print(kljuc, vrednost)


def kljuc_najvecje_vrednosti(slovar):
    kljuc_najvecje = None
    najvecja = None
    for kljuc, vrednost in slovar.items():
        if najvecja == None or vrednost > najvecja:
            najvecja = vrednost
            kljuc_najvecje = kljuc

    return kljuc_najvecje


def pojavitve_znakov(niz):
    pojavitve = {}

    for znak in niz:
        if znak not in pojavitve:
            pojavitve[znak] = 0

        pojavitve[znak] = pojavitve[znak] + 1

    return pojavitve


besedilo = """Kot je dejal, bi po izvedbi demokratičnih volitev v Ukrajini na oblast prišla kompetentna vlada, ki bi bila sposobna delati v smeri sklenitve mirovnega sporazuma. "S tem bi nato začeli pogajanja o mirovnem sporazumu, podpisali legitimne dokumente, ki so priznani po vsem svetu ter so varni in stabilni," je dodal.

Dejal je, da prizadevanja ameriškega predsednika Donalda Trumpa za nadaljevanje neposrednih pogovorov z Rusijo – v nasprotju z njegovim predhodnikom Joejem Bidnom, ki se je stikom izogibal – kažejo, da si novi predsednik želi miru. "Menim, da si novoizvoljeni predsednik ZDA iz več razlogov iskreno želi končati konflikt," so njegove besede povzele tiskovne agencije.

Trump je dejal, da želi posredovati za hiter konec vojne, vendar vrsta pogovorov še ni prinesla bistvene spremembe v sovražnostih med državama.

"""
