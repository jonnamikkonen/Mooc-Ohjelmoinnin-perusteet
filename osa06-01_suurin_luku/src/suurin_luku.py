# tee ratkaisu tänne
def suurin():
    luvut = []
    with open ("luvut.txt") as tiedosto:
        for rivi in tiedosto:
            luvut.append(int(rivi))
        if len(luvut) > 0:
            suurin = luvut[0]
            for luku in luvut:
                if luku > suurin:
                    suurin = luku
            return suurin

if __name__ == "__main__":
    print(suurin())