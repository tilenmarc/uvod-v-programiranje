from bs4 import BeautifulSoup
import re
import json

dat = open("filmi.html")
vsebina = dat.read()
dat.close()


juha = BeautifulSoup(vsebina, "html.parser")

filmi = []
for najdba in juha.find_all("li", attrs={"class": "ipc-metadata-list-summary-item"}):
    link = najdba.find("h3")

    leto = najdba.find("li", attrs={"class": "ipc-inline-list__item"})

    leto = leto.text.strip()
    n2 = re.search(r"(\d{4})", leto)
    leto = int(n2[1])

    filmi.append({"naslov": link.text.strip(), "leto": leto})


# print(len(filmi))


dat = open("top250.json", "w")
json.dump(filmi, dat)
dat.close()
