import requests
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}


def pridobi_htmlje(stevilo_strani):
    for i in range(1, stevilo_strani + 1):
        odgovor = requests.get(
            f"https://www.goodreads.com/list/show/1.Best_Books_Ever?page={i}",
            headers=HEADERS,
        )
        if odgovor.status_code != 200:
            print("napaka", i)
            continue

        vsebina = odgovor.text
        dat = open(f"stran{i}.html", "w")
        dat.write(vsebina)
        dat.close()

        time.sleep(1)


def pridobi_htmlje_knjig(osnovni_podatki):
    htmlji_knjig = []

    for podatek in osnovni_podatki:
        for _ in range(10):
            odgovor = requests.get(
                podatek["povezava"],
                headers=HEADERS,
            )
            if odgovor.status_code != 200:
                print("napaka", odgovor.status_code, podatek["povezava"])
                continue
            else:
                break

        if odgovor.status_code != 200:
            print("preskocil", podatek["povezava"])
            continue

        vsebina_knjiga = odgovor.text

        htmlji_knjig.append(vsebina_knjiga)

    return htmlji_knjig
