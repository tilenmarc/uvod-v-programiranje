def moj_range(n):
    seznam = []
    i = 0
    while i < n:
        seznam.append(i)
        i += 1

    return seznam


def moj_range_bolje(n):
    i = 0
    while i < n:
        yield i
        i += 1
