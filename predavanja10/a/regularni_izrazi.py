import re

datoteka = open("filmi.html")

besedilo = datoteka.read()

datoteka.close()


def poisci_naslov(besedilo, naslov):
    while True:
        indeks_zacetka = besedilo.find(naslov)
        if indeks_zacetka == -1:
            return
        print(besedilo[indeks_zacetka - 20 : indeks_zacetka + len(naslov) + 20])
        print(20 * " " + len(naslov) * "*")

        besedilo = besedilo[indeks_zacetka + 1 :]


def poisci_filme(besedilo):
    vzorec = re.compile(
        r"<a href=\"https://www.imdb.com/title/tt(?P<id>\d+)/.*?>"
        r"(?P<pozicija>\d+)\. (?P<naslov>.+?)</h3></a>.+?>"
        r"(?P<leto>\d+)<"
    )

    filmi = []
    for najdba in vzorec.finditer(besedilo):
        # print(besedilo[najdba.start() : najdba.end()])
        film = {
            "naslov": najdba["naslov"],
            "id": najdba["id"],
            "pozicija": int(najdba["pozicija"]),
            "leto": int(najdba["leto"]),
        }
        filmi.append(film)

    return filmi
