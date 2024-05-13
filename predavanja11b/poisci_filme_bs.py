from bs4 import BeautifulSoup

filmi = []
with open("filmi.html") as dat:
    besedilo = dat.read()

    soup = BeautifulSoup(besedilo, "html.parser")

    for znacka in soup.findAll("a", attrs={"class": "ipc-title-link-wrapper"}):
        film = {"naslov": znacka.text, "link": znacka["href"]}
        filmi.append(film)

print(filmi)
print(len(filmi))
