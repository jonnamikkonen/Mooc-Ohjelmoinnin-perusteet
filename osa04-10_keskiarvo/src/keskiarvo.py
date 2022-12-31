# tee ratkaisu tänne
def keskiarvo(lista: list):
    summa = float(sum(lista))
    vastaus = float(summa/len(lista))
    return float(vastaus)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [1, 3, 67, 7, 4, 23, 1, 5, 7, 4]
    tulos = float(keskiarvo(lista)) 
    print(float(tulos))
