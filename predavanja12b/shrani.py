import csv


def shrani(podatki):
    with open("filmi.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "id",
                "naslov",
                "leto",
                "ocena",
                "oznaka",
                "cas",
                "opis",
                "cena",
                "zasluzek",
            ]
        )
        for podatek in podatki:
            pisatelj.writerow(
                [
                    podatek["id"],
                    podatek["naslov"],
                    podatek["leto"],
                    podatek["ocena"],
                    podatek["oznaka"],
                    podatek["cas"],
                    podatek["opis"],
                    podatek["cena"],
                    podatek["zasluzek"],
                ]
            )

    with open("osebe.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id", "ime"])
        ids = set()
        for podatek in podatki:
            for igralec in podatek["igralci"]:
                if igralec[0] not in ids:
                    pisatelj.writerow([igralec[0], igralec[1]])
                    ids.add(igralec[0])
            for reziser in podatek["reziserji"]:
                if reziser[0] not in ids:
                    pisatelj.writerow([reziser[0], reziser[1]])
                    ids.add(reziser[0])

    with open("osebe_filmi.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_igralca", "id_filma", "vloga"])
        for podatek in podatki:
            for igralec in podatek["igralci"]:
                pisatelj.writerow([igralec[0], podatek["id"], "I"])
            for reziser in podatek["reziserji"]:
                pisatelj.writerow([reziser[0], podatek["id"], "R"])

    with open("filmi_zanri.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_filma", "zanr"])
        for podatek in podatki:
            for zanr in podatek["zanri"]:
                pisatelj.writerow([podatek["id"], zanr])
