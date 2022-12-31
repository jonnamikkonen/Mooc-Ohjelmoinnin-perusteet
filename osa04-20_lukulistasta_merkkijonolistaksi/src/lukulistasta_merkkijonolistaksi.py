# tee ratkaisu tänne
def muotoile(lista: float):
    lista2 = []
    for numero in lista:
        numero = f"{numero:.2f}"
        lista2.append(numero)
        
    return (lista2)
    


if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)