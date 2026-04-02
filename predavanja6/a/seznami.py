sez = ["a", "b"]
sez2 = ["c", "d"]

for i, el in enumerate(sez):
    print(i, el)


for el1, el2 in zip(sez, sez2):
    print(el1, el2)
