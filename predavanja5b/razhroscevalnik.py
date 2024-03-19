temperatura = 10


def izracun(x):
    if x == 0:
        return 0

    # print("vmesna vrednost", x)

    return temperatura + izracun(x - 1)


print(izracun(5))
