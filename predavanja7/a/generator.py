def moj_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


def moj_neskoncni_range():
    i = 0
    while True:
        yield i
        i += 1
