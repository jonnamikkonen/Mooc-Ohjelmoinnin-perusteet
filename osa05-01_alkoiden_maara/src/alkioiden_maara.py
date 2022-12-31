# tee ratkaisu tänne
def laske_alkiot(matriisi: list, alkio: int):
    muuttuja = 0
    for rivi in matriisi:
        for i in rivi:
            if i == alkio:
                muuttuja +=1
    return muuttuja


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))