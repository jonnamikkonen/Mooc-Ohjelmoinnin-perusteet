# tee ratkaisu tänne
def samat(mjono, luku1, luku2):
    if luku2 >= len(mjono):
        return False
    elif luku1 >= len(mjono):
        return False
    elif mjono[luku1] == mjono[luku2]:
        return True
    else:
        return False
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("abc", 0, 3)) 