import json

student = {
    "ime": "Janez",
    "priimek": "Novak",
    "predmeti": [{"predmet": "UVP", "ocen": 10}, {"predmet": "Algebra", "ocena": 9}],
}

with open("student.json", "w") as dat:
    json.dump(student, dat)


with open("student.json") as dat:
    student = json.load(dat)

    print(student)
