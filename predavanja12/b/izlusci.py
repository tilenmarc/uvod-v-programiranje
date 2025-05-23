import os
import re


vzorec = re.compile(
    r'<a href="/title/tt(?P<sifra>\d+)/\?ref_=sr_t_.+?" class="ipc-title-'
    r'link-wrapper" tabindex=".+?"><h3 '
    r'class="ipc-title__text">\d+. (?P<naslov>.+?)</h3></a>'
)


def izlusci_osnovno(od, do):
    filmi_osnovno = []
    for leto in range(od, do):
        with open(os.path.join("filmi", f"filmi{leto}.html")) as dat:
            besedilo = dat.read()
            for najdba in vzorec.finditer(besedilo):
                filmi_osnovno.append((najdba["naslov"], najdba["sifra"]))

    return filmi_osnovno


def izlusci_filme(filmi_osnovno):
    filmi_info = []
    for film in filmi_osnovno:
        naslov = film[0]
        sifra = film[1]
        igralici_v_filmu = []

        leto = ""
        oznaka = ""
        cas = ""

        with open(os.path.join("filmi", f"film{sifra}.html")) as dat:
            besedilo = dat.read()

        # izluscimo igralce
        igralci_re = re.compile(
            r'ipc-metadata-list-item__list-content-item--link" tabindex=".+?" '
            r'aria-disabled="false" href="/name/nm(?P<sifra>\d+)/\?ref_=tt_ov_st_.+?">(?P<ime>.+?)</a></li>'
        )

        for najdba in igralci_re.finditer(besedilo):
            igralec = (najdba["sifra"], najdba["ime"])
            if igralec not in igralici_v_filmu:
                igralici_v_filmu.append(igralec)

        if len(igralici_v_filmu) == 0:
            print("napaka: igralci", sifra)

        # izluscimo leto, oznako in cas
        lastosti_re = re.compile(
            r'aria-disabled="false" href="/title/tt\d+/releaseinfo/\?ref_=tt_ov_rdat">'
            r"(.*?)"
            r'</a>(.*?)class="ipc-inline-list__item">((\d+?h ?)?(\d+?m)?)</li></ul></div>'
        )
        najdba = lastosti_re.search(besedilo)
        if najdba is not None:
            leto = najdba.group(1)[0:4]
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
            print("napaka: lastnosti", sifra)

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
                print("napaka: reziserji", sifra)
        else:
            print("napaka: reziserji", sifra)

        # izluscimo oceno
        rating_re = re.compile(r'__aggregate-rating__score".+?>(\d.\d)</span>')
        najdba = rating_re.search(besedilo)
        if najdba is not None:
            ocena = najdba.group(1)
        else:
            print("napaka: ocena", sifra)

        # izluscimo zanre
        zanri = []
        zanri_re = re.compile(
            r'href="/interest/.+?/\?ref_=tt_ov_in_\d"><span class="ipc-chip__text">(.+?)</span>'
        )
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
            print("napaka: opis", sifra)

        # izluscimo ceno produkcije
        cena_re = re.compile(r'productionBudget":{"budget":{"amount":(\d+)')
        najdba = cena_re.search(besedilo)
        if najdba is not None:
            cena = najdba.group(1)
        else:
            cena = ""
            print("napaka: cena", sifra)

        # izluscimo zasluzek
        zasluzek_re = re.compile(r"Gross worldwide</span><div.+?>\$(.+?)</span>")
        najdba = zasluzek_re.search(besedilo)
        if najdba is not None:
            zasluzek = int(najdba.group(1).replace(",", ""))
        else:
            zasluzek = ""
            print("napaka: zasluzek", sifra)

        filmi_info.append(
            {
                "id": sifra,
                "naslov": naslov,
                "igralci": igralici_v_filmu,
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
        )

    return filmi_info
