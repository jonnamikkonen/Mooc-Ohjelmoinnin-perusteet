# tee ratkaisu tänne
def uniikit(lista:list):
    lista1 = []
    käytetyt =[]
    for numero in lista:
        if numero in lista1:
            käytetyt.append(numero)
            
        else:    
            lista1.append(numero)
            
    return sorted(lista1)


if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))