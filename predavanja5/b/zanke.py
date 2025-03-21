import random


def priblizek_pi(n):
    stevec = 0
    for _ in range(n):
        x = 2 * random.random() - 1
        y = 2 * random.random() - 1
        if x**2 + y**2 <= 1:
            stevec += 1

    return (stevec / n) * 4
