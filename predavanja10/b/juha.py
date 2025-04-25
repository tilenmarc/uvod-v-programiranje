from bs4 import BeautifulSoup
import re

datoteka = open("filmi.html")
besedilo = datoteka.read()
datoteka.close()


juha = BeautifulSoup(besedilo, "html.parser")


filmi = []
for znacka_li in juha.findAll("li", attrs={"class": "ipc-metadata-list-summary-item"}):
    film = {}
    for znacka_a in znacka_li.findAll("a"):
        film["naslov"] = znacka_a.text
        povezava = znacka_a["href"]
        film["povezava"] = povezava

        sifra = re.search("\d+", povezava)

        film["sifra"] = sifra[0]

    filmi.append(film)

print(filmi)
print(len(filmi))
