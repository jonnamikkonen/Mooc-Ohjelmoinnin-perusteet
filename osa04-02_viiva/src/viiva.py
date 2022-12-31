# tee ratkaisu tänne
def viiva(leveys, mjono):
    if len(mjono) >0:
        print(mjono[0:1]*leveys)
    elif len(mjono) == 0:
        print("*"*leveys)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "x")
