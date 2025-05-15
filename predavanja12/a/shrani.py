import csv


def shrani_filme(filmi):
    with open("filmi.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "id",
                "naslov",
                "ocena",
                "cas",
                "leto",
                "oznaka",
                "opis",
                "cena",
                "zasluzek",
            ]
        )

        for film in filmi:
            pisatelj.writerow(
                [
                    film["id"],
                    film["naslov"],
                    film["ocena"],
                    film["cas"],
                    film["leto"],
                    film["oznaka"],
                    film["opis"],
                    film["cena"],
                    film["zasluzek"],
                ]
            )


def shrani_osebe(filmi):
    with open("osebe.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "id",
                "ime",
            ]
        )

        ze_videni = set()
        for film in filmi:
            for oseba in film["igralci"] + film["reziserji"]:
                if oseba in ze_videni:
                    continue

                pisatelj.writerow(
                    [
                        oseba[0],
                        oseba[1],
                    ]
                )
                ze_videni.add(oseba)


def shrani_povezovalno_osebe_filmi(filmi):
    with open("osebe_filmi.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_filma", "id_igralca", "vloga"])

        for film in filmi:
            for igralec in film["igralci"]:
                pisatelj.writerow([film["id"], igralec[0], "I"])

            for reziser in film["reziserji"]:
                pisatelj.writerow([film["id"], reziser[0], "R"])


def shrani_povezovalno_filmi_zanri(filmi):
    with open("filmi_zanri.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["id_filma", "zanr"])

        for film in filmi:
            for zanr in film["zanri"]:
                pisatelj.writerow([film["id"], zanr])
