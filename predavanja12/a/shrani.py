import csv


def shrani_knjige(knjige):
    dat = open("knjige.csv", "w")
    pisatelj = csv.writer(dat)
    pisatelj.writerow(
        [
            "id",
            "naslov",
            "id_avtorja",
            "povprecna_ocena",
            "stevilo_ocen",
            "stevilo_recenzij",
            "stevilo_strani",
            "jezik",
            "leto_izdaje",
            "trenutno_bere",
            "opis",
        ]
    )

    dat2 = open("avtorji.csv", "w")
    pisatelj2 = csv.writer(dat2)
    pisatelj2.writerow(["id", "ime"])

    dat3 = open("zanri.csv", "w")
    pisatelj3 = csv.writer(dat3)
    pisatelj3.writerow(["id_knjige", "zanr"])

    videni_avtorj = set()

    for knjiga in knjige:
        pisatelj.writerow(
            [
                knjiga["id"],
                knjiga["naslov"],
                knjiga["id_avtorja"],
                knjiga["povprecna_ocena"],
                knjiga["stevilo_ocen"],
                knjiga["stevilo_recenzij"],
                knjiga["stevilo_strani"],
                knjiga["jezik"],
                knjiga["leto_izdaje"],
                knjiga["trenutno_bere"],
                knjiga["opis"],
            ]
        )
        if knjiga["id_avtorja"] not in videni_avtorj:
            videni_avtorj.add(knjiga["id_avtorja"])
            pisatelj2.writerow([knjiga["id_avtorja"], knjiga["avtor"]])

        for zanr in knjiga["zanri"]:
            pisatelj3.writerow([knjiga["id"], zanr])

    dat.close()
    dat2.close()
    dat3.close()
