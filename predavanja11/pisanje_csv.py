import csv


with open("test.csv", "w") as dat:
    pisatelj = csv.writer(dat)
    pisatelj.writerow(["ime", "vpisna"])

    for i in range(10):
        pisatelj.writerow([f"ime{i}", i])
