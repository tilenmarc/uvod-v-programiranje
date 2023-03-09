import math


def integriraj_sinus(a, b, n):
    epsilon = (b - a) / n
    vsota = 0
    x = a
    for _ in range(n):
        vsota += math.sin(x) * epsilon
        x += epsilon

    return vsota


def integriraj(f, a, b, n):
    epsilon = (b - a) / n
    vsota = 0
    x = a
    for _ in range(n):
        vsota += f(x) * epsilon
        x += epsilon

    return vsota


def kvadrat(x):
    return x**2


# integriraj(kvadrat, 0, 3, 10000)

import random


def aproksimiraj_pi(n):
    v_krogu = 0
    for i in range(1, n + 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            v_krogu += 1
        print(v_krogu * 4 / i)

    return v_krogu * 4 / n


def nicla_funkcije(f, a, b, epsilon):
    """Poisci niclo zvezne funkcije f med a in b,
    kjer velja, da je f(a) * f(b) < 0."""

    while b - a > epsilon:
        sredina = (a + b) / 2
        f_od_sredina = f(sredina)
        if f_od_sredina == 0:
            return sredina
        elif f_od_sredina * f(a) > 0:
            a = sredina
        else:
            b = sredina

    return (a + b) / 2


def narisi_implicitni_graf(f, a, b, c, d, n):
    for i in range(n):
        for j in range(n):
            x = a + (i * (b - a) / n)
            y = c + (j * (d - c) / n)
            if abs(f(x, y)) < 0.2:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


def kroznica(x, y):
    return x**2 + y**2 - 1


# narisi_implicitni_graf(kroznica, -2, 2, -2, 2, 20)
