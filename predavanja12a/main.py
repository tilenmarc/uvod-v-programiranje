import pridobi
import poisci_filme
import izlusci
import shrani

od, do = 1980, 1985

pridobi.pridobi_filme(od, do)

vsi_filmi = []
for leto in range(od, do):
    filmi = poisci_filme.poisci(leto)
    vsi_filmi.extend(filmi)

vsi_podatki = []
for film in vsi_filmi:
    id = film[1]
    naslov = film[0]
    pridobi.pridobi_film(id)
    podatki = izlusci.izlusci_film(id)
    vsi_podatki.append((id, naslov) + podatki)


shrani.shrani_podatke(vsi_podatki)
