import re

datoteka = open("filmi.html")
besedilo = datoteka.read()
datoteka.close()

# print(besedilo)


def poisci_naslov(besedilo, naslov):
    while True:
        indeks_zacetka = besedilo.find(naslov)
        if indeks_zacetka == -1:
            return
        print(besedilo[indeks_zacetka - 20 : indeks_zacetka + len(naslov) + 20])
        print(20 * " " + len(naslov) * "*")

        besedilo = besedilo[indeks_zacetka + 1 :]


# poisci_naslov(besedilo, "Star Wars")


vzorec = re.compile(
    r'<a href="https://www.imdb.com/title/tt(?P<sifra>\d+)'
    r"/\?ref_=chttp.+?>(?P<pozicija>\d+)\. (?P<naslov>.+?)</h3>"
    r'</a></div>.+?"IMDb rating: (?P<ocena>.+?)"'
)


def poisci_filme(besedilo):
    filmi = []
    for najdba in vzorec.finditer(besedilo):
        film = {
            "naslov": najdba["naslov"],
            "sifra": najdba["sifra"],
            "ocena": float(najdba["ocena"]),
            "pozicija": int(najdba["pozicija"]),
        }
        filmi.append(film)

    return filmi


filmi = poisci_filme(besedilo)
print(filmi)
print(len(filmi))
