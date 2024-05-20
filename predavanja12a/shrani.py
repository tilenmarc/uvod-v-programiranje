import json
import csv


def shrani_podatke(podatki):
    with open("filmi.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id", "naslov", "leto", "oznaka", "cas", "ocena"])
        for podatek in podatki:
            pisatelj.writerow(
                [podatek[0], podatek[1], podatek[6], podatek[7], podatek[5], podatek[4]]
            )


def shrani_podatke_json(podatki):
    with open("filmi.json", "w") as dat:
        json.dump(podatki, dat)
