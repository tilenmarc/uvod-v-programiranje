def stevilo_razlicnih_besed(ime_datoteke):
    razlicne_besede = set()
    with open(ime_datoteke, encoding="utf-8") as dat:
        vrstice = dat.readlines()
        for vrstica in vrstice:
            vrstica = vrstica.strip()
            besede = vrstica.split(" ")
            for beseda in besede:
                razlicne_besede.add(beseda)

    return len(razlicne_besede)
