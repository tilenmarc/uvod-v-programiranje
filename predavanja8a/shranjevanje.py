import json

seznam = ["bla", "bla"]
slovar = {"seznam": seznam}

with open("nekaj.json", "w") as dat:
    json.dump(slovar, dat)

with open("nekaj.json") as dat:
    slovar = json.load(dat)
    print(slovar)
