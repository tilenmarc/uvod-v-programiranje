def prestej_crke(ime_datoteke):
    stevilo_crk = 0

    dat = open(ime_datoteke)
    besedilo = dat.read()

    for znak in besedilo:
        if znak.isalpha():
            stevilo_crk += 1

    dat.close()

    return stevilo_crk


def prestej_crke_loceno(ime_datoteke):
    stevilo_crk = {}

    with open(ime_datoteke) as dat:
        besedilo = dat.read()

        for znak in besedilo:
            znak = znak.lower()
            if znak.isalpha():
                stevilo_crk[znak] = stevilo_crk.get(znak, 0) + 1

    return stevilo_crk


def prestej_besede_loceno(ime_datoteke):
    stevilo_besed = {}

    with open(ime_datoteke, encoding="utf-8") as dat:
        for vrstica in dat:
            vrstica = vrstica.replace(".", "")
            vrstica = vrstica.replace(",", "")
            vrstica = vrstica.replace("\n", "")
            vrstica = vrstica.replace(";", "")
            vrstica = vrstica.replace("!", "")
            vrstica = vrstica.lower()
            besede = vrstica.split(" ")
            for beseda in besede:
                stevilo_besed[beseda] = stevilo_besed.get(beseda, 0) + 1

    return stevilo_besed


def prepisi_na_glas(ime_datoteke, nova_datoteka):
    with open(ime_datoteke, encoding="utf-8") as dat:
        vsebina = dat.read()

    vsebina = vsebina.upper()

    with open(nova_datoteka, "w", encoding="utf-8") as dat:
        dat.write(vsebina)
