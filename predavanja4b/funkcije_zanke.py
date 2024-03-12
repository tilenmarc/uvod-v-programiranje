import random


def pi_priblizek(n):
    stevec = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            stevec += 1

    return (stevec / n) * 4


def implicitni_graf(f, x1, x2, y1, y2, n):
    for i in range(n):
        for j in range(n):
            x = x1 + i * (x2 - x1) / n
            y = y1 + j * (y2 - y1) / n

            if abs(f(x, y)) < 0.2:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


def kroznica(x, y):
    return x**2 + y**2 - 1


def f_mandelbrot(z, w, x, y):
    return z**2 - w**2 + x, 2 * z * w + y


def mandelbrot(x, y):
    z = 0
    w = 0
    for _ in range(1000):
        z, w = f_mandelbrot(z, w, x, y)
        if z**2 + w**2 > 100:
            return 1
    return 0
