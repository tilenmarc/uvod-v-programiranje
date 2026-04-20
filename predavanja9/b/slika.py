from PIL import Image


def uredi(ime_slika):
    slika = Image.open(ime_slika)

    nova = Image.new("RGB", (slika.width, slika.height))

    for i in range(slika.width):
        for j in range(slika.height):
            nova.putpixel((i, j), slika.getpixel((slika.width - 1 - i, j)))

    nova.save("nova" + ime_slika)
