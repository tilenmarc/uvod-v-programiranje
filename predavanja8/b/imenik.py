import os


def izpisi_repozitorij(lokacija, zamik=0):
    vsebina = os.listdir(lokacija)
    vsebina.sort()
    for element in vsebina:
        if element[0] in "._":
            continue
        print(zamik * " " + element)
        if os.path.isdir(os.path.join(lokacija, element)):
            izpisi_repozitorij(os.path.join(lokacija, element), zamik + 2)
