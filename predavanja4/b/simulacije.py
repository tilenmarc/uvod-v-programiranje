import random


def oceni_pi(n):
    stevec = 0
    for _ in range(n):
        x = random.random()
        x = 2 * x - 1
        y = random.random()
        y = 2 * y - 1

        if x**2 + y**2 <= 1:
            stevec += 1

    return (stevec / n) * 4


def mandelbrot_f(z1, z2, c1, c2):
    return (z1**2 - z2**2 + c1, 2 * z1 * z2 + c2)


def ponovi(z1, z2, c1, c2, n):
    if n == 0:
        return z1, z2

    noviz1, noviz2 = mandelbrot_f(z1, z2, c1, c2)

    if noviz1**2 + noviz2**2 > 500:
        return noviz1, noviz2

    return ponovi(noviz1, noviz2, c1, c2, n - 1)


def mandelbrot(x, y):
    z1, z2 = ponovi(0, 0, x, y, 100)
    if z1**2 + z2**2 > 500:
        return 1
    else:
        return 0


def oceni_mandelbrot(n):
    stevec = 0
    for _ in range(n):
        x = random.random()
        x = 4 * x - 2
        y = random.random()
        y = 4 * y - 2

        if mandelbrot(x, y) == 0:
            stevec += 1

    return (stevec / n) * 16


def nakljucni_sprehod(n, m):
    for _ in range(n):
        pozicija = 0
        stevec = 0
        for _ in range(m):
            korak = random.randint(0, 1)
            korak = 2 * korak - 1

            pozicija += korak

            if pozicija == 0:
                stevec += 1
                break

    return stevec / n


def nakljucni_sprehod_2d(n, m):
    stevec = 0
    for _ in range(n):
        pozicija_x = 0
        pozicija_y = 0
        for _ in range(m):
            korak = 1 if random.random() < 0.5 else -1

            os = random.randrange(2)
            if os == 0:
                pozicija_x += korak
            else:
                pozicija_y += korak

            if pozicija_x == 0 and pozicija_y == 0:
                stevec += 1
                break

    return stevec / n
