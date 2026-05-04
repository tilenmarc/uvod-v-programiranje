import re
import json

dat = open("filmi.html")
vsebina = dat.read()
dat.close()


def poisci_naslov(naslov, vsebina):
    vsebina = vsebina.replace("\n", "")
    indeks = 0
    while True:
        indeks2 = vsebina[indeks + 1 :].find(naslov)
        if indeks2 == -1:
            break

        print(vsebina[indeks - 50 : indeks + len(naslov) + 50])
        print(50 * " " + len(naslov) * "*")
        indeks += indeks2 + 1
        print(indeks, indeks2)


def izlusci_filme(vsebina):
    filmi = []
    for najdba in re.finditer(
        r'<a\s*href="https://www\.imdb\.com/title/tt(?P<id>\d+)/.*?text">\s*(?P<naslov>.*?)\s*</h3></a.*?<li.*?(?P<leto>\d+)',
        vsebina,
        flags=re.DOTALL,
    ):
        filmi.append(
            {
                "naslov": najdba["naslov"],
                "id": najdba["id"],
                "leto": int(najdba["leto"]),
            }
        )

    return filmi


filmi = izlusci_filme(vsebina)

leta = [film["leto"] for film in filmi]
print(sum(leta) / len(leta))

dat = open("filmi.json", "w")
json.dump(filmi, dat)
dat.close()
