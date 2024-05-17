import re


def izlusci_film(id):
    with open(f"filmi/film{id}.html") as dat:
        besedilo = dat.read()

    # izluscimo igralce
    igralci_re = re.compile(
        r'title-cast-item__actor" href="/name/nm(?P<id>\d+)/\?ref_=tt_cl_t_\d+" class="sc-bfec09a1-1 gCQkeh">(?P<ime>.+?)</a>'
    )
    igralci = []
    for najdba in igralci_re.finditer(besedilo):
        igralci.append((najdba["id"], najdba["ime"]))
    if len(igralci) == 0:
        print("napaka: igralci", id)

    # izluscimo leto, oznako in cas
    lastosti_re = re.compile(
        r'href="/title/tt\d+/releaseinfo\?ref_=tt_ov_rdat">(\d+)</a></li>'
        r"(.*?)"
        r'<li role="presentation" class="ipc-inline-list__item">((\d+?h ?)?(\d+?m)?)</li>'
    )
    najdba = lastosti_re.search(besedilo)
    leto = ""
    oznaka = ""
    cas = ""
    if najdba is not None:
        leto = najdba.group(1)
        oznaka_del = najdba.group(2)
        oznaka_re = re.compile(r'<li role="presentation".+?tt_.+?">(.+?)</a></li>')
        najdba2 = oznaka_re.search(oznaka_del)
        if najdba2 is not None:
            oznaka = najdba2.group(1)
        cas_tekst = najdba.group(3)
        # spremenimo cas v minute
        cas_re = re.compile(r"(\d*)h? ?(\d*)m?")
        najdba3 = cas_re.search(cas_tekst)
        cas = 60 * int("0" + najdba3.group(1)) + int("0" + najdba3.group(2))

    else:
        print("napaka: lastnosti", id)

    # izluscimo reziserje
    reziserji = []
    reziserji_re = re.compile(r'directors?":\[(.+?)\]')
    najdba = reziserji_re.search(besedilo)
    if najdba is not None:
        reziser_re = re.compile(
            r'{"@type":"Person","url":"https://www.imdb.com/name/nm(\d+)/","name":"(.+?)"}'
        )
        for najdba2 in reziser_re.finditer(najdba.group(1)):
            id_osebe = najdba2.group(1)
            ime = najdba2.group(2)
            reziserji.append((id_osebe, ime))
        if len(reziserji) == 0:
            print("napaka: reziserji", id)
    else:
        print("napaka: reziserji", id)

    # izluscimo oceno
    rating_re = re.compile(r'__aggregate-rating__score".+?>(\d.\d)</span>')
    najdba = rating_re.search(besedilo)
    if najdba is not None:
        ocena = najdba.group(1)
    else:
        print("napaka: ocena", id)

    # izluscimo zanre
    zanri = []
    zanri_re = re.compile(r'href="/search/title\?genres=(.+?)&')
    for najdba in zanri_re.finditer(besedilo):
        zanr = najdba.group(1)
        zanri.append(zanr)

    # izluscimo opis
    opis_re = re.compile(r'"image":.*?"description":"(.+?)"')
    najdba = opis_re.search(besedilo)
    if najdba is not None:
        opis = najdba.group(1)
    else:
        opis = ""
        print("napaka: opis", id)

    # izluscimo ceno produkcije
    cena_re = re.compile(r'productionBudget":{"budget":{"amount":(\d+)')
    najdba = cena_re.search(besedilo)
    if najdba is not None:
        cena = najdba.group(1)
    else:
        cena = ""
        print("napaka: cena", id)

    # izluscimo zasluzek
    zasluzek_re = re.compile(r"Gross worldwide</span><div.+?>\$(.+?)</span>")
    najdba = zasluzek_re.search(besedilo)
    if najdba is not None:
        zasluzek = int(najdba.group(1).replace(",", ""))
    else:
        zasluzek = ""
        print("napaka: zasluzek", id)

    return {
        "igralci": igralci,
        "reziserji": reziserji,
        "ocena": ocena,
        "cas": cas,
        "leto": leto,
        "oznaka": oznaka,
        "zanri": zanri,
        "opis": opis,
        "cena": cena,
        "zasluzek": zasluzek,
    }
