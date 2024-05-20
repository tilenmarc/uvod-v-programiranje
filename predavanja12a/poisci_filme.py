import re
import os


def poisci(leto):
    with open(os.path.join("filmi", f"filmi{leto}.html")) as dat:
        besedilo = dat.read()
        niz = r'<a href="/title/tt(?P<id>\d+)/\?ref_.*?<h3 class="ipc-title__text">\d+. (?P<naslov>.+?)</h3>'
        filmi = []
        for najdba in re.finditer(niz, besedilo):
            filmi.append((najdba["naslov"], najdba["id"]))

    return filmi
