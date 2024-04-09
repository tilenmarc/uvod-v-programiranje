def prestej_crke(datoteka):
    """Presteje stevilo crk v datoteki."""
    with open(datoteka, encoding="utf-8") as dat:
        tekst = dat.read()

        stevec = 0
        for znak in tekst:
            if znak.isalpha():
                stevec += 1

    return stevec


def prestej_besede(datoteka):
    """Presteje stevilo besed v datoteki."""
    with open(datoteka, encoding="utf-8") as dat:
        vrstice = dat.readlines()

        stevec = 0
        for vrstica in vrstice:
            besede = vrstica.split(" ")
            for beseda in besede:
                if len(beseda) >= 3:
                    stevec += 1

    return stevec


def prestej_razlicne_besede(datoteka):
    """Presteje stevilo razlicnih besed v datoteki."""
    with open(datoteka, encoding="utf-8") as dat:
        vrstice = dat.readlines()

        ze_videne = set()
        stevec = 0
        for vrstica in vrstice:
            besede = vrstica.split(" ")
            for beseda in besede:
                if beseda in ze_videne:
                    continue
                if len(beseda) >= 3:
                    ze_videne.add(beseda)
                    stevec += 1

    return stevec


def shrani_na_glas(datoteka, nova_datoteka):
    with open(datoteka, encoding="utf-8") as dat:
        with open(nova_datoteka, "w", encoding="utf-8") as dat_nova:
            tekst = dat.read()
            dat_nova.write(tekst.upper())
