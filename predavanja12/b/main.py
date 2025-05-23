import pobiranje
import izlusci
import shrani
import sys

od = 1950
do = 2025


if __name__ == "__main__":
    argumenti = sys.argv
    poberi = True
    if len(argumenti) > 1 and argumenti[1] == "ne_poberi":
        poberi = False

    if poberi:
        pobiranje.poberi_osnovno(od, do)
    filmi_osnovno = izlusci.izlusci_osnovno(od, do)

    if poberi:
        pobiranje.poberi_filme(filmi_osnovno)
    filmi = izlusci.izlusci_filme(filmi_osnovno)

    print(len(filmi))

    shrani.shrani_filme(filmi)
