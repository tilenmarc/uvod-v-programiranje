import matplotlib.pyplot as plt
import time


# V O(n)
def ali_vsebuje(x, sez):
    return x in sez


# V O(n)
def ali_vsebuje_urejen(x, sez):
    if len(sez) == 0:
        return False
    if len(sez) == 1:
        return x == sez[0]

    sredina = len(sez) // 2
    sredinska_vrednost = sez[sredina]
    if x == sredinska_vrednost:
        return True

    if x < sredinska_vrednost:
        return ali_vsebuje_urejen(x, sez[0:sredina])

    else:
        return ali_vsebuje_urejen(x, sez[sredina + 1 :])


# V O(log(n))
def ali_vsebuje_urejen_bolje(x, sez):
    zacetek = 0
    konec = len(sez)
    while True:
        if (konec - zacetek) == 0:
            return False
        if (konec - zacetek) == 1:
            return x == sez[zacetek]

        sredina = (konec + zacetek) // 2
        sredinska_vrednost = sez[sredina]
        if x == sredinska_vrednost:
            return True
        elif x < sredinska_vrednost:
            konec = sredina
        else:
            zacetek = sredina + 1


x = range(0, 1000000, 10000)
y = []
ponovitev = 100
for i in x:
    sez = [j for j in range(i)]
    zacetek = time.time()
    for _ in range(ponovitev):
        # ali_vsebuje(-1, sez)
        # ali_vsebuje_urejen(-1, sez)
        ali_vsebuje_urejen_bolje(-1, sez)
    konec = time.time()
    y.append((konec - zacetek) / ponovitev)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel="dolzina seznama", ylabel="cas", title="Casovna zahtevnost")
ax.grid()

fig.savefig("test.png")
plt.show()
