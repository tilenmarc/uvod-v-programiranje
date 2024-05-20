import requests
import os
import time


def pridobi_filme(od, do):
    for leto in range(od, do):
        url = f"https://www.imdb.com/search/title/?title_type=feature&release_date={leto}-01-01,{leto}-12-31&groups=oscar_winner&sort=user_rating,desc"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.5",
        }
        odgovor = requests.get(url, headers=headers)
        if odgovor.status_code != 200:
            print("napaka")
            continue
        with open(os.path.join("filmi", f"filmi{leto}.html"), "w") as dat:
            dat.write(odgovor.text)
        # time.sleep(1)


def pridobi_film(id):
    url = f"https://www.imdb.com/title/tt{id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
    }
    odgovor = requests.get(url, headers=headers)
    if odgovor.status_code != 200:
        print("napaka")
        return
    with open(os.path.join("filmi", f"film{id}.html"), "w") as dat:
        dat.write(odgovor.text)
