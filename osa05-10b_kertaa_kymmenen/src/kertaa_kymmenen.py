# tee ratkaisu tänne
def kertaa_kymmenen(alku: int, loppu: int):
    kerrat = alku-1
    sanakirja = {}
    while kerrat < loppu:
        kerrat += 1
        sanakirja[alku] = alku*10
        alku += 1
        
    return sanakirja


if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)