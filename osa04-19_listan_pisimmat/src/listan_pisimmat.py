# tee ratkaisu tänne
def pisimmat(lista: list):
    pisin = 0
    lista2 = []

    for muuttuja in lista:
        if len(muuttuja) > pisin:
            pisin = len(muuttuja)
    
    for muuttuja in lista:
        if len(muuttuja) == pisin:
            lista2.append(muuttuja)
    return lista2

if __name__ == "__main__":
    lista = ['Arto', 'Matti', 'kissa', 'koira']
    print(pisimmat(lista))
    