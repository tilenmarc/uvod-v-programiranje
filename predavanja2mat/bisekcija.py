import math


def predznak(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def nicle_sinusa(a, b, epsilon=10 ** (-10)):
    """Funkcija naj vrne niclo sinusa
    na intervalu [a, b], kjer predpostavljamo,
    da predznak(sin(a)) != predznak(sin(b))"""

    if b - a < epsilon:
        return (a + b) / 2

    levo_krajisce = math.sin(a)
    sredisce = math.sin((a + b) / 2)
    if sredisce == 0:
        return (a + b) / 2

    if predznak(sredisce) != predznak(levo_krajisce):
        return nicle_sinusa(a, (a + b) / 2, epsilon)
    else:
        return nicle_sinusa((a + b) / 2, b, epsilon)
