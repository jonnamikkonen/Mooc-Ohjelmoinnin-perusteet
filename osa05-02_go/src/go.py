# tee ratkaisu tänne
def kumpi_voitti(pelilauta: list):
    muuttuja = 0
    muuttuja1 = 0
    muuttuja2 = 0
    for rivi in pelilauta:
        for ruutu in rivi:
            if ruutu == 1:
                muuttuja1 += 1
            if ruutu == 2:
                muuttuja2 += 1
            if ruutu == 0:
                muuttuja += 1
    if muuttuja1 > muuttuja2:
        muuttuja1 = 1
        return muuttuja1
    if muuttuja2 > muuttuja1:
        muuttuja2 = 2
        return muuttuja2
    if muuttuja1 == muuttuja2:
        muuttuja = 0
        return muuttuja

if __name__ == "__main__":
    pelilauta = [[1, 2, 2, 2], [0, 0, 0, 1], [0, 0, 2, 1]]
    tulos = kumpi_voitti(pelilauta)
    print(tulos)