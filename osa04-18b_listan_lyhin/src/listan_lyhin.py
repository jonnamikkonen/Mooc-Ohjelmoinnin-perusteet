# tee ratkaisu tänne
def lyhin(lista):
    muuttuja = 0

    while True:
        for sana in lista:
            if muuttuja == len(sana):
                return sana
                break
        muuttuja +=1
        
if __name__ == "__main__":
    lista = ['Arto', 'Matti']

    tulos = lyhin(lista)
    print(tulos)