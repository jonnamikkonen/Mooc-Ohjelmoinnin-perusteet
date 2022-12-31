# tee ratkaisu tänne
def eniten_kirjainta(mjono):
    lista = {}
    for i in mjono:
        if i in lista:
            lista[i] += 1
        else:
            lista[i] = 1
    tulos = max(lista, key = lista.get)

    return tulos

if __name__ == "__main__":
    mjono = "abbbbcccc"
    print(eniten_kirjainta(mjono))