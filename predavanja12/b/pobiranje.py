import requests
import os


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


def poberi_osnovno(od, do):
    for leto in range(od, do):
        odgovor = requests.get(
            f"https://www.imdb.com/search/title/?release_date={leto}-01-01,{leto}-12-31&groups=oscar_winner",
            headers=headers,
        )
        if odgovor.status_code != 200:
            print("napaka", leto)
            continue

        with open(os.path.join("filmi", f"filmi{leto}.html"), "w") as dat:
            dat.write(odgovor.text)


def poberi_filme(filmi_osnovno):
    for film in filmi_osnovno:
        sifra = film[1]
        odgovor = requests.get(
            f"https://www.imdb.com/title/tt{sifra}/", headers=headers
        )
        if odgovor.status_code != 200:
            print("napaka", sifra)
            continue

        with open(os.path.join("filmi", f"film{sifra}.html"), "w") as dat:
            dat.write(odgovor.text)
