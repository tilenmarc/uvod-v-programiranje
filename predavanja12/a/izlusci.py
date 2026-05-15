import re
import html
import datetime

vzorec = re.compile(
    r'<a\s+class="bookTitle"[^>]*href="(?P<link>/book/show/(?P<id_knjige>\d+)[^"]*)"[^>]*>'
    r"\s*<span[^>]*>(?P<naslov>.*?)</span>",
    re.DOTALL,
)


def osnovni_podatki(stevilo_strani):
    osnovi = []
    stevec = 0
    for i in range(1, stevilo_strani + 1):
        dat = open(f"stran{i}.html")
        vsebina = dat.read()
        dat.close()

        for najdba in vzorec.finditer(vsebina):
            # if stevec >= 3:
            #     break
            print(stevec)
            stevec += 1

            povezava = "https://www.goodreads.com" + najdba["link"]

            info = {
                "naslov": najdba["naslov"],
                "povezava": povezava,
                "id": najdba["id_knjige"],
            }

            osnovi.append(info)

    return osnovi


def podrobnosti_knjig(osnovni_podatki, htmlji_knjig):
    knjige = []
    for i, html_vsebina in enumerate(htmlji_knjig):
        knjige.append(izloci_podrobnosti_o_knjigi(html_vsebina) | osnovni_podatki[i])

    return knjige


def izloci_podrobnosti_o_knjigi(vsebina):
    avtor_re = re.search(
        r'<a[^>]*class="[^"]*ContributorLink[^"]*"[^>]*>\s*<span[^>]*>(.*?)</span>',
        vsebina,
        re.DOTALL,
    )
    avtor_link_re = re.search(
        r'href="https://www\.goodreads\.com/author/show/(?P<id_avtorja>\d+)[^"]*"',
        vsebina,
    )
    ocena_re = re.search(r'"ratingValue"\s*:\s*([0-9]+(?:\.[0-9]+)?)', vsebina)
    st_ocen_re = re.search(r'"ratingCount"\s*:\s*(\d+)', vsebina)
    st_recenzij_re = re.search(r'"reviewCount"\s*:\s*(\d+)', vsebina)
    st_strani_re = re.search(r'"numberOfPages"\s*:\s*(\d+)', vsebina)
    jezik_re = re.search(r'"inLanguage"\s*:\s*"([^"]+)"', vsebina)
    trenutni_bralci_re = re.search(
        r"([\d,]+)\s+people\s+are\s+currently\s+reading", vsebina
    )
    opis_re = re.search(
        r'<div[^>]*data-testid="description"[^>]*>.*?<span[^>]*class="Formatted"[^>]*>(.*?)</span>',
        vsebina,
        re.DOTALL,
    )

    publication_time_re = re.search(r'"publicationTime":\s*(\d+)', vsebina)
    if publication_time_re:
        timestamp = int(publication_time_re.group(1)) / 1000
        leto_izdaje = datetime.datetime.fromtimestamp(timestamp, datetime.UTC).year
    else:
        leto_izdaje = None

    zanri_del_re = re.search(r'"bookGenres":\s*\[(.*?)\]', vsebina, re.DOTALL)
    if zanri_del_re:
        zanri = re.findall(r'"name":"(.*?)"', zanri_del_re.group(1))
        zanri = [pocisti_besedilo(zanr) for zanr in zanri]
    else:
        zanri = []

    return {
        "id_avtorja": int(avtor_link_re.group("id_avtorja")) if avtor_link_re else None,
        "avtor": pocisti_besedilo(avtor_re.group(1)) if avtor_re else None,
        "povprecna_ocena": float(ocena_re.group(1)) if ocena_re else None,
        "stevilo_ocen": int(st_ocen_re.group(1).replace(",", "")) if st_ocen_re else 0,
        "stevilo_recenzij": (
            int(st_recenzij_re.group(1).replace(",", "")) if st_recenzij_re else 0
        ),
        "stevilo_strani": int(st_strani_re.group(1)) if st_strani_re else None,
        "jezik": jezik_re.group(1) if jezik_re else None,
        "leto_izdaje": leto_izdaje,
        "trenutno_bere": (
            int(trenutni_bralci_re.group(1).replace(",", ""))
            if trenutni_bralci_re
            else 0
        ),
        "zanri": zanri,
        "opis": pocisti_opis(opis_re.group(1)) if opis_re else None,
    }


def pocisti_besedilo(besedilo):
    if besedilo is None:
        return None
    return html.unescape(" ".join(besedilo.split()))


def pocisti_opis(opis):
    if opis is None:
        return None

    opis = re.sub(r"<br\s*/?>", "\n", opis)
    opis = re.sub(r"</p\s*>", "\n", opis)
    opis = re.sub(r"<[^>]+>", "", opis)
    opis = html.unescape(opis)
    opis = " ".join(vrstica.strip() for vrstica in opis.splitlines())
    opis = re.sub(r"\s+", " ", opis)
    return opis.strip()
