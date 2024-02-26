a = 5
b = 6

if a < b:
    print(10)


def absolutna_vrednost(x):
    if x >= 0:
        return x
    else:
        return -x


def predznak(x):
    if x > 0:
        return 1
    else:
        if x < 0:
            return -1
        else:
            return 0


def predznak2(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
