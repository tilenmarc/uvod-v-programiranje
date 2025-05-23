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
