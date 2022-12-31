# tee ratkaisu tähän
def tulosta_monesti(merkkijono, kertaa):
    rivit = 0
    while rivit < kertaa:
        print(merkkijono)
        rivit += 1
    
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    tulosta_monesti("python", 5)