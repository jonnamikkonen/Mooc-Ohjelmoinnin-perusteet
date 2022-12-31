# tee ratkaisu tänne
def summa(lista1, lista2):
    
    list1 = []
    list2 = []

    for numero1 in lista1:
        list1.append(numero1)
    for numero2 in lista2:
        list2.append(numero2)

    zipped_lists = zip(list1, list2)


    summa = [x + y for (x, y) in zipped_lists]


    return summa


if __name__ == "__main__":
    lista1 = [1, 2, 3]
    lista2 = [7, 8, 9]
    print(summa(lista1, lista2))