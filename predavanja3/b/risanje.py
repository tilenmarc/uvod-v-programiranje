def zvezdice(n):
    if n == 0:
        return

    print(n * "*")
    zvezdice(n - 1)


def zvezdice_obrnjeno(n, zacni=1):
    if n == 0:
        return
    print(zacni * "*")

    zvezdice_obrnjeno(n - 1, zacni + 1)


def vmes(n, m):
    if n == 0:
        return

    print("*" + (m - 2) * " " + "*")

    vmes(n - 1, m)


def kvadrat(n):
    print(n * "*")

    vmes(n - 2, n)

    print(n * "*")


def kvadrat2(n):
    print(n * "*")

    print((n - 2) * ("*" + (n - 2) * " " + "*\n"), end="")

    print(n * "*")


def narisi_vrstico(f, x1, x2, y1, n):
    if n == 0:
        print("")
        return

    if abs(f(x1, y1)) < 0.1:
        print("*", end="")
    else:
        print(" ", end="")

    narisi_vrstico(f, x1 + ((x2 - x1) / n), x2, y1, n - 1)


def implicitni_graf(f, x1, x2, y1, y2, n, m):
    if m == 0:
        return

    narisi_vrstico(f, x1, x2, y2, n)

    implicitni_graf(f, x1, x2, y1, y2 + ((y1 - y2) / m), n, m - 1)


def ponovi(f, n, w, z, x, y):
    if n == 0:
        return w, z
    w, z = ponovi(f, n - 1, w, z, x, y)
    if w**2 + z**2 > 2:
        return w, z

    return f(w, z, x, y)


def mandelbrot_f(w, z, x, y):
    prva = w**2 - z**2 + x
    druga = 2 * w * z + y

    return prva, druga


def mandelbrot(x, y):
    w, z = 0, 0

    w, z = ponovi(mandelbrot_f, 500, w, z, x, y)

    if w**2 + z**2 > 2:
        return 1
    else:
        return 0


def mandelbrot2(x, y):
    w, z = 0, 0

    for _ in range(500):
        w, z = mandelbrot_f(w, z, x, y)
        if w**2 + z**2 > 2:
            return 1
    else:
        return 0
