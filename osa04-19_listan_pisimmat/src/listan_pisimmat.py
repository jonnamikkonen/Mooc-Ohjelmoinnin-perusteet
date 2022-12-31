# tee ratkaisu tänne
def pisimmat(lista):
    pisin = max(lista, key=len)
    return pisin

if __name__ == "__main__":
    lista = ['Arto', 'Matti', 'kissa', 'koira']
    print(pisimmat(lista))
    