# tee ratkaisu tänne
def shakkilauta(x):
    merkit = ["0", "1"]

    for i in range(x):
        for r in range(x):
            muuttuja = merkit[(i + r + 1) % 2]
            print(muuttuja, end=(""))
        print()
# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)
