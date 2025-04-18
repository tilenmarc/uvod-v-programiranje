import random
import time
import matplotlib.pyplot as plt


def ali_vsebuje(x, sez):
    for el in sez:
        if el == x:
            return True

    return False


def ali_vebuje_urejen(x, sez):
    zacetek = 0
    konec = len(sez)

    while True:
        if konec - zacetek <= 0:
            return False
        elif konec - zacetek == 1:
            return x == sez[zacetek]

        sredina = (konec + zacetek) // 2
        element = sez[sredina]
        if x == element:
            return True
        elif x < element:
            konec = sredina
        else:
            zacetek = sredina + 1


def poisci_najmanjsega(sez):
    najmanjsi = None
    indeks = None
    for i, el in enumerate(sez):
        if najmanjsi == None or najmanjsi > el:
            najmanjsi = el
            indeks = i

    return najmanjsi, indeks


def uredi_seznam(sez):
    """Vrne nov seznam, ki ima elemente urejene po
    velikosti."""
    urejen = []

    while len(sez) > 0:
        najmanjsi, indexs = poisci_najmanjsega(sez)
        urejen.append(najmanjsi)
        sez = sez[:indexs] + sez[indexs + 1 :]

    return urejen


velikosti = list(range(0, 3000, 100))
casi = []

for velikost in velikosti:
    print(velikost)
    seznam = [random.randint(0, 1000000) for _ in range(velikost)]

    # ali_vsebuje(42, seznam)
    urejen = uredi_seznam(seznam)
    zacetek = time.time()
    for _ in range(1000):
        ali_vebuje_urejen(42, urejen)
    konec = time.time()

    casi.append((konec - zacetek) / 1000)

# print(casi)

fig, ax = plt.subplots()
ax.plot(velikosti, casi)
ax.set(xlabel="velikost", ylabel="cas", title="Racunska zahtevnost")
ax.grid()

plt.show()
