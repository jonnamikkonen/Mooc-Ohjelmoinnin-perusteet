# tee ratkaisu tänne
def parilliset(lista: list):
    alkuperainen = []
    parilliset = []

    for numero in lista:
        if numero % 2 == 0: #parillinen
            alkuperainen.append(numero)
            
        else: 
            parilliset.append(numero)
            
    return alkuperainen
    return parilliset
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)