import re


filmi = []
with open("filmi.html") as dat:
    besedilo = dat.read()

    izraz = re.compile(
        r'<a href="https://www.imdb.com/title/tt(?P<id>\d+).+?'
        r'<h3 class="ipc-title__text">\d+\. (?P<naslov>.+?)</h3>.+?'
        r"IMDb rating: (?P<ocena>\d+\.\d)"
    )
    for najdba in izraz.finditer(besedilo):
        film = {
            "naslov": najdba["naslov"],
            "id": int(najdba["id"]),
            "ocena": float(najdba["ocena"]),
        }
        filmi.append(film)

print(filmi)
print(len(filmi))
