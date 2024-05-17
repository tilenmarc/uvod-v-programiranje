import pridobi
import poisci_filme
import izlusci
import shrani

od, do = 1980, 1990


# pridobi.pridobi(od, do)

vsi_filmi = []
for leto in range(od, do):
    filmi = poisci_filme.poisci(leto)
    vsi_filmi.extend(filmi)

vsi_podatki = []
for film in vsi_filmi:
    id = film[1]
    naslov = film[0]
    # pridobi.pridobi_film(id)
    podatki = izlusci.izlusci_film(id)
    podatki["naslov"] = naslov
    podatki["id"] = id
    vsi_podatki.append(podatki)

shrani.shrani(vsi_podatki)
