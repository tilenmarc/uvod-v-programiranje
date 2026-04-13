import random


def zbrisi(m, i, j):
    nov_m = []
    for k in range(len(m)):
        if k != i:
            nov_m.append(m[k][:j] + m[k][j + 1 :])

    return nov_m


def det(m):
    """Matrika m je n x n."""
    if len(m) == 1:
        return m[0][0]

    d = 0

    for j in range(len(m[0])):  # O(n)
        d += m[0][j] * det(zbrisi(m, 0, j)) * (-1) ** j  # O(n**2) + rekurzija

    return d


def nakljucna_matrika(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]


def sestej_vrstici(s1, s2, k):
    return [s1[i] + k * s2[i] for i in range(len(s1))]


def zamenjaj_vrstici(m, i, j):
    m[i], m[j] = m[j], m[i]


# O(n**3)
def det_gauss(m):
    zamenjave = 0

    for i in range(len(m)):  # O(n)
        m_ii = m[i][i]
        if m_ii == 0:
            for j in range(i + 1, len(m)):  # O(n)
                if m[j][i] != 0:
                    m_ii = m[j][i]
                    zamenjaj_vrstici(m, i, j)  # O(1)
                    zamenjave += 1
                    break
            else:
                return 0

        for j in range(i + 1, len(m)):  # O(n)
            m_ji = m[j][i]
            m[j] = sestej_vrstici(m[j], m[i], -m_ji / m_ii)  # O(n)

    d = 1
    for i in range(len(m)):
        d *= m[i][i]

    return d * (-1) ** zamenjave
