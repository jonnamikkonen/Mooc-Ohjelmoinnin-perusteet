# tee ratkaisu tänne
def positiivisten_summa(lista: list):
    omalista = []
    for numero in lista:
        if numero >= 0:
            omalista.append(numero)
    summa = int(sum(omalista))
    return summa
    
if __name__ == "__main__":
    lista = [1, -2, 3, -4, 5]
    print("vastaus:", positiivisten_summa(lista))
    