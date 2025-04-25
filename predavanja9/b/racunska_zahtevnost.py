import random
import time
import matplotlib.pyplot as plt


def ali_vsebuje(sez, x):
    return x in sez


def zbrisi(mat, i, j):
    nova_mat = []
    for k in range(len(mat)):
        if k == i:
            continue
        nova_vrstica = [mat[k][l] for l in range(len(mat[k])) if l != j]
        nova_mat.append(nova_vrstica)

    return nova_mat


def determinanta(mat):
    """Vrne determinanto n x n matrike."""
    if len(mat) == 1:
        return mat[0][0]

    det = 0
    for i in range(len(mat[0])):
        m_1i = mat[0][i]

        nova_mat = zbrisi(mat, 0, i)

        det += m_1i * determinanta(nova_mat) * (-1) ** (i)

    return det


def vsota_vrstic(vrstica1, vrstica2):
    return [vrstica1[i] + vrstica2[i] for i in range(len(vrstica1))]


def konstanta_krat_vrstic(c, vrstica):
    return [c * vrstica[i] for i in range(len(vrstica))]


def determinanta_gauss(mat):
    """Vrne determinanto n x n matrike s
    pomocjo Gaussove eliminacije."""

    det_povecal = 1

    n = len(mat)
    for i in range(n):
        m_ii = mat[i][i]

        for j in range(i + 1, n):
            m_ji = mat[j][i]
            mat[j] = vsota_vrstic(
                konstanta_krat_vrstic(m_ii, mat[j]),
                konstanta_krat_vrstic(-m_ji, mat[i]),
            )
            det_povecal *= m_ii

    det = 1
    for i in range(n):
        det *= mat[i][i]

    return det / det_povecal


# mat = [[1, 1, 1], [0, 1, 2], [0, 0, 1]]

# print(determinanta(mat))

# for i in range(1, 20):
#     velikost = i

#     # seznam = [random.randint(0, 10000000) for _ in range(velikost)]
#     matrika = [
#         [random.randint(0, 10000000) for _ in range(velikost)] for _ in range(velikost)
#     ]

#     print(determinanta(matrika))
#     print(determinanta_gauss(matrika))


velikosti = []
casi_izvajanja = []

for i in range(1, 150):
    velikost = i

    # seznam = [random.randint(0, 10000000) for _ in range(velikost)]
    matrika = [
        [float(random.randint(0, 100000)) for _ in range(velikost)]
        for _ in range(velikost)
    ]
    # x = 42

    zacetek = time.time()
    for _ in range(1):
        # ali_vsebuje(seznam, x)
        # determinanta(matrika)
        determinanta_gauss(matrika)
    konec = time.time()

    velikosti.append(velikost)
    casi_izvajanja.append(konec - zacetek)


fig, ax = plt.subplots()
ax.plot(velikosti, casi_izvajanja)

ax.set(xlabel="velikost", ylabel="cas", title="Casovna zahtevnost")
ax.grid()

plt.show()
