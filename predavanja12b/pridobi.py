import requests
import os


def pridobi(od, do):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }

    for leto in range(od, do):
        url = f"https://www.imdb.com/search/title/?title_type=feature&release_date={leto}-01-01,{leto}-12-31&groups=oscar_winner&sort=user_rating,desc"

        odgovor = requests.get(url, headers=headers)
        if odgovor.status_code != 200:
            print("napaka", leto, odgovor.status_code)
            return

        with open(os.path.join("filmi", f"filmi{leto}.html"), "w") as dat:
            dat.write(odgovor.text)


def pridobi_film(id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }

    url = f"https://www.imdb.com/title/tt{id}"

    odgovor = requests.get(url, headers=headers)
    if odgovor.status_code != 200:
        print("napaka", id, odgovor.status_code)
        return

    with open(os.path.join("filmi", f"film{id}.html"), "w") as dat:
        dat.write(odgovor.text)
