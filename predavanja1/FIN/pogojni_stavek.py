a = 0
if a < 3:
    a = a + 1
print(a)


def absolutna_vrednost(x):
    if x >= 0:
        rezultat = x
    else:
        rezultat = -x

    return rezultat


def predznak(x):
    if x > 0:
        return 1
    else:
        if x == 0:
            return 0
        else:
            return -1


def predznak2(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1
