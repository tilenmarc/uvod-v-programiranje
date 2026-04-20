import os

# for i in range(1000):
#     dat = open(f"dat{i}.txt", "w")
#     dat.write("UVP")
#     dat.close()

# for i in range(1000):
#     os.remove(f"dat{i}.txt")


def izpisi_imenik(lokacija, zamik=0):
    vsebina = os.listdir(lokacija)
    vsebina.sort()
    for x in vsebina:
        if x[0] == "." or x[:2] == "__":
            continue
        je_datoteka = os.path.isfile(os.path.join(lokacija, x))

        print(zamik * " " + x)
        if not je_datoteka:
            izpisi_imenik(os.path.join(lokacija, x), zamik + 2)


def poisci_datoteke(lokacija):
    datoteke = []

    vsebina = os.listdir(lokacija)
    for x in vsebina:
        if x[0] == "." or x[:2] == "__":
            continue
        je_datoteka = os.path.isfile(os.path.join(lokacija, x))

        if je_datoteka:
            velikost = os.path.getsize(os.path.join(lokacija, x))

            datoteke.append((x, velikost))
        else:
            datoteke_v_dir = poisci_datoteke(os.path.join(lokacija, x))

            datoteke.extend(datoteke_v_dir)

    datoteke.sort(key=lambda x: -x[1])

    return datoteke
