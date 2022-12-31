# tee ratkaisu tänne
def rivisummat ():
    with open ("matriisi.txt") as tiedosto:
        matriisi = []
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            alkiot = rivi.split(",")

            luvut = []
            for alkio in alkiot:
                luvut.append(int(alkio))
                tulos = sum(luvut)

                matriisi.append(tulos)

    return matriisi

def summa():
    rivisumma2 = rivisummat()
    matriisinsumma = sum(rivisumma2)
    return matriisinsumma

def maksimi():
    rivisummat()
    suurin = max(rivisummat)

if __name__ == "__main__":
    rivisumma = rivisummat()
    kokonaissumma = summa()
    suurin = maksimi()
    print(rivisummat, summa, suurin)