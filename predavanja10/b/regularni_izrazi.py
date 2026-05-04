import re

dat = open("filmi.html")
vsebina = dat.read()
dat.close()


filmi = []
for najdba in re.finditer(
    r'<a\s+href="https://www\.imdb\.com/title/'
    r'tt(?P<id>\d+)/\?ref.+?text">\s*(?P<naslov>.+?)\s*</h3></a'
    r'.*?item"\s+>\s+(?P<leto>\d*)\s+</li>',
    vsebina,
    flags=re.DOTALL,
):
    filmi.append(
        {"naslov": najdba["naslov"], "id": najdba["id"], "leto": int(najdba["leto"])}
    )

print(filmi)
print(len(filmi))

import matplotlib.pyplot as plt

plt.scatter([i for i in range(1, len(filmi) + 1)], [film["leto"] for film in filmi])
plt.savefig("graf.png")
