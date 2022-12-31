# tee ratkaisu tänne
def risunelio (x):
    risuaita = "#"*x
    rivit = 0
    while rivit < x:
        print(risuaita)
        rivit += 1
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)