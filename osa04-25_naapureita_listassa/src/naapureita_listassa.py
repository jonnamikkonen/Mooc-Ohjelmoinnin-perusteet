# tee ratkaisu tänne
def pisin_naapurijono(lista:list):
    muuttuja = 0
    for numero in lista:
        numero1 = numero
        for numero in lista:
            if numero1-numero != 1:
                break
            if numero1-numero == 1:
                muuttuja +=1
        
    print(muuttuja)



if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))