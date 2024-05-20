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
        cas = 0
        ure_re = re.compile(r"(\d*)h")
        najdba3 = ure_re.search(cas_tekst)
        if najdba3 is not None:
            cas = 60 * int(najdba3.group(1))
        minute_re = re.compile(r"(\d*)m")
        najdba3 = minute_re.search(cas_tekst)
        if najdba3 is not None:
            cas += int(najdba3.group(1))

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

    return (igralci, reziserji, ocena, cas, leto, oznaka)
