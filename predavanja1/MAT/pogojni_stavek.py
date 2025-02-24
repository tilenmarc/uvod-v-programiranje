a = 8
b = 6

if a < b:
    a = a + 1
else:
    a = a - 1

print(a)


def absolutna_vrednost(x):
    if x >= 0:
        return x
    else:
        return -x


def predznak(x):
    """Vrne 1, ce pozitiven, 0 ce enak 0 in -1,
    ce negativen."""
    if x > 0:
        return 1
    else:
        if x < 0:
            return -1
        else:
            return 0


def predznak2(x):
    """Vrne 1, ce pozitiven, 0 ce enak 0 in -1,
    ce negativen."""
    predznak = 0

    if x > 0:
        predznak = 1
    elif x < 0:
        predznak = -1
    else:
        predznak = 0

    return predznak
