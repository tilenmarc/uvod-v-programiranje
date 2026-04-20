import os

for i in range(100):
    dat = open(f"dat{i}.txt", "w")
    dat.write("kar neki")
    dat.close()

for i in range(100):
    os.remove(f"dat{i}.txt")


pot = os.path.join("predavanja9", "a", "krst-pri-savici.txt")
dat = open(pot)
dat.close()


print(os.path.lis)
