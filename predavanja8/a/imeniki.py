import os

print(os.getcwd())

os.path.join

dat = open(os.path.join("predavanja8", "a", "krst-pri-savici.txt"))
# dat2 = open(
#     "/home/janeznovak/git/uvod-v-programiranje/predavanja8/a/krst-pri-savici.txt"
# )

os.chdir("predavanja8")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
