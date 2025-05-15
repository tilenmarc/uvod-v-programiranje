import pridobi
import izlusci
import shrani
import sys

od = 1950
do = 2025

argumenti = sys.argv
poberi = True
if len(argumenti) > 1 and argumenti[1] == "ne_poberi":
    poberi = False

if poberi:
    pridobi.shrani_osnovne_htmlje_o_filmih(od, do)

osnovni_podatki = izlusci.izlusci_osnovne_podatke(od, do)

if poberi:
    pridobi.shrani_htmlje_o_filmih(osnovni_podatki)

filmi = izlusci.izlusci_podatke_o_filmih(osnovni_podatki)

shrani.shrani_filme(filmi)
shrani.shrani_osebe(filmi)
shrani.shrani_povezovalno_osebe_filmi(filmi)
shrani.shrani_povezovalno_filmi_zanri(filmi)
