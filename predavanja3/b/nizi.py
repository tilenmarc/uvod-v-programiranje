import random


def stevilo_samoglasnikov(niz):
    """Vrne stevilo samoglasnikov v nizu."""
    if len(niz) == 0:
        return 0

    stevilo = 0
    if niz[0] in "aeiouAEIOU":
        stevilo += 1

    stevilo += stevilo_samoglasnikov(niz[1:])

    return stevilo


def zamenjaj_samoglasnike_z_vprasaji(niz):
    if len(niz) == 0:
        return ""

    if niz[0] in "aeiouAEIOU":
        nov_niz = "?"
    else:
        nov_niz = niz[0]

    nov_niz += zamenjaj_samoglasnike_z_vprasaji(niz[1:])

    return nov_niz


def super_AI_bot():
    print("Zivjo, jaz sem AI bot, klici me Janez. Kako se imenujes?")

    ime = input()

    print(f"Zdravo, {ime}. Vprasaj me karkoli?")

    input()

    neumno_vprasanje()


def neumno_vprasanje():
    x = random.choice("abc")

    if x == "a":
        print("to vprasanje ni zanimivo. Vprasaj kaj drugega")
    if x == "b":
        print("zanimivo, ampak sem bolj strokovnjak za matematiko")
    if x == "c":
        print("super vprasanje, bom razmislil. Vmes me vprasaj se kaj drugega")

    input()

    neumno_vprasanje()


def narisi_kvadrat(n):
    print(n * "*")
    ponovi_m_krat(n - 2, n)
    print(n * "*")


def ponovi_m_krat(m, n):
    if m == 0:
        return

    print("*" + ((n - 2) * " ") + "*")

    ponovi_m_krat(m - 1, n)


def graf_implicitne_funkcije(f, x1, x2, y1, y2, n, m):
    if m == 0:
        return

    narisi_vrstico(f, x1, x2, y2, n)

    graf_implicitne_funkcije(f, x1, x2, y1, y2 - ((y2 - y1) / m), n, m - 1)


def narisi_vrstico(f, x1, x2, y2, n):
    if n == 0:
        print("")
        return

    if abs(f(x1, y2)) < 0.1:
        print("*", end="")
    else:
        print(" ", end="")

    narisi_vrstico(f, x1 + ((x2 - x1) / n), x2, y2, n - 1)


def kroznica(x, y):
    return x**2 + y**2 - 1


def polinom(x, y):
    return y - x * (x - 1) * (x + 1)


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
