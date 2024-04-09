import os


def izpisi_imenik(pot, zamik=0):
    vsebina = os.listdir(pot)
    vsebina.sort()
    for element in vsebina:
        if element[0] in "._":
            continue
        if os.path.isfile(os.path.join(pot, element)):
            print(zamik * " " + element)
        if os.path.isdir(os.path.join(pot, element)):
            print(zamik * " " + element)

            izpisi_imenik(os.path.join(pot, element), zamik + 2)
