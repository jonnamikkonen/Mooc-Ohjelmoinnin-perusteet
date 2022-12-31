# tee ratkaisu tänne
def suurin():
    with open ("luvut.txt") as tiedosto:
        for rivi in tiedosto:
            suurin = max(tiedosto)
        return int(suurin)

if __name__ == "__main__":
    print(suurin())