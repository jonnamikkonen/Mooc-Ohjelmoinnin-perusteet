# tee ratkaisu tänne
def pisimman_pituus(lista):
    max = len(lista[0])

    for sana in lista:
        if(len(sana) > max):
 
            max = len(sana)
    return max
 
 
if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = pisimman_pituus(lista)
    print(tulos)