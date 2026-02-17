a = 9
if a < 8 and a > 1:
    a = a + 1
else:
    a = a + 5

print(a)


def absolutna_vrednost(x):
    if x < 0:
        return -x
    else:
        return x


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
