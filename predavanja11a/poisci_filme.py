import re

with open("filmi.html") as dat:
    besedilo = dat.read()
    niz = r'<a href="https://www.imdb.com/title/tt(?P<id>\d+)/\?ref_.*?<h3 class="ipc-title__text">\d+. (?P<naslov>.+?)</h3>'
    filmi = []
    for najdba in re.finditer(niz, besedilo):
        filmi.append((najdba["naslov"], int(najdba["id"])))

print(filmi, len(filmi))
