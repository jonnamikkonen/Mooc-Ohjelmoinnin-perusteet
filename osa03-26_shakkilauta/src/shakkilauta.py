# tee ratkaisu tänne
def shakkilauta(x):
    i = x
    while i > 0:
        a = x
        k = 1
        while a > 0:
            if k == 1:
                print(k, end="")
                k = 0
                a -= 1
            else:
                print(k, end="")
                k = 1
                a -= 1
            print()
            i -= 1
# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)
