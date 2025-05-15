import requests
import re
import time
import os

od = 1980
do = 1985

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

for leto in range(od, do):
    odgovor = requests.get(
        f"https://www.imdb.com/search/title/?release_date={leto}-01-01,{leto}-12-31&groups=oscar_winner",
        headers=headers,
    )
    if odgovor.status_code != 200:
        print("napaka", leto)
        continue

    with open(os.path.join("filmi", f"filmi{leto}.html"), "w") as dat:
        dat.write(odgovor.text)


vzorec = re.compile(
    r'<a href="/title/tt(?P<sifra>\d+)/\?ref_=sr_t_.+?" class="ipc-title-'
    r'link-wrapper" tabindex=".+?"><h3 '
    r'class="ipc-title__text">\d+. (?P<naslov>.+?)</h3></a>'
)

filmi = []
for leto in range(od, do):
    with open(os.path.join("filmi", f"filmi{leto}.html")) as dat:
        besedilo = dat.read()
        for najdba in vzorec.finditer(besedilo):
            filmi.append((najdba["naslov"], najdba["sifra"]))


for film in filmi:
    sifra = film[1]
    odgovor = requests.get(f"https://www.imdb.com/title/tt{sifra}/", headers=headers)
    if odgovor.status_code != 200:
        print("napaka", leto)
        continue

    with open(os.path.join("filmi", f"film{sifra}.html"), "w") as dat:
        dat.write(odgovor.text)

    time.sleep(1)


vzorec = re.compile(
    r'ipc-metadata-list-item__list-content-item--link" tabindex=".+?" '
    r'aria-disabled="false" href="/name/nm(?P<sifra>\d+)/\?ref_=tt_ov_st_.+?">(?P<ime>.+?)</a></li>'
)

vsi_igralci = []
for film in filmi:
    igralici_v_filmu = []
    sifra = film[1]

    with open(os.path.join("filmi", f"film{sifra}.html")) as dat:
        besedilo = dat.read()
        for najdba in vzorec.finditer(besedilo):
            igralec = (najdba["ime"], najdba["sifra"], film[1])
            if igralec not in igralici_v_filmu:
                igralici_v_filmu.append(igralec)

    vsi_igralci.append(igralici_v_filmu)
