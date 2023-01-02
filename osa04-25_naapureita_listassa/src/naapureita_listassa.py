# tee ratkaisu tänne
def pisin_naapurijono(lista: list):
    naapurit = len(lista)
    muuttuja1 = 0
    muuttuja2 = 0
    for i in range(naapurit - 1):
        if abs(lista[i] - lista[i + 1]) == 1:
            muuttuja1 += 1
        else:
            muuttuja1 = 0
            
        if muuttuja1 > muuttuja2:
            muuttuja2 = muuttuja1
    return muuttuja2 + 1


if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))