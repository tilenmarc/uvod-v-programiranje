def pogovor():
    print("Dobrodosli, kako vam je ime?")
    ime = input()

    print(f"{ime} je lepo ime. Kaj boste narocili?")
    kajse()


def kajse():
    narocilo = input()
    print(f"Ok, {narocilo}, kaj se?")
    kajse()
