import pridobi
import izlusci
import shrani
import sys

STEVILO_STRANI = 10

if len(sys.argv) > 1 and sys.argv[1] == "pridobi":
    pridobi.pridobi_htmlje(STEVILO_STRANI)

osnovni_podatki = izlusci.osnovni_podatki(STEVILO_STRANI)

htmlji_knjig = pridobi.pridobi_htmlje_knjig(osnovni_podatki)

knjige = izlusci.podrobnosti_knjig(osnovni_podatki, htmlji_knjig)

shrani.shrani_knjige(knjige)
