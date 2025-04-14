def povej_na_glas(ime_datoteke, nova_datoteka):
    with open(ime_datoteke, encoding="utf-8") as dat:
        vsebina = dat.read()

    nova_vsebina = vsebina.upper()
    nova_vsebina = nova_vsebina.replace(".", "!")

    with open(nova_datoteka, "w", encoding="utf-8") as nova_dat:
        nova_dat.write(nova_vsebina)
