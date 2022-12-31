# tee ratkaisu tänne
def lista_tahtina(lista: list):
    merkki = "*"
    for numero in lista:
        tahti= numero*merkki
        print(tahti)
    
if __name__ == "__main__":
    lista_tahtina([3, 7, 1, 1, 2])
    