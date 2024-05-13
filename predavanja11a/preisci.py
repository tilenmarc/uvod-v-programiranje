import re


def poisci_vse(niz, besedilo):
    seznam_indeksov = []
    zacetek = 0
    indeks = 0
    while True:
        indeks = besedilo.find(niz, zacetek)
        if indeks == -1:
            break
        seznam_indeksov.append(indeks)
        zacetek = indeks + 1

    return seznam_indeksov


def pokazi(niz, besedilo):
    indeksi = poisci_vse(niz, besedilo)
    for indeks in indeksi:
        print(besedilo[indeks - 20 : indeks + len(niz) + 20])
        print(20 * " " + len(niz) * "*")


def pokazi_re(niz, besedilo):
    najdbe = re.finditer(niz, besedilo)
    for najdba in najdbe:
        print(besedilo)
        print(najdba.start() * " " + (najdba.end() - najdba.start()) * "*")
