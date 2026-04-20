def prestej_besede(ime_datoteke):
    s = {}

    with open(ime_datoteke) as dat:
        vsebina = dat.read()
        vsebina = vsebina.replace(",", "")
        vsebina = vsebina.replace(".", "")
        vsebina = vsebina.replace("!", "")
        vsebina = vsebina.replace(";", "")
        vsebina = vsebina.replace("\n", " ")
        vsebina = vsebina.replace("?", "")

        besede = vsebina.split(" ")

        for beseda in besede:
            if beseda == "":
                continue
            beseda = beseda.lower()
            if beseda not in s:
                s[beseda] = 1
            else:
                s[beseda] += 1

    return s
