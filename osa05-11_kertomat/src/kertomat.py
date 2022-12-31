# tee ratkaisu tänne
def kertomat(n: int):
    kertoma = 0 
    sanakirja = {}
    tulo = 1

    while True:
        if kertoma == n:
            break
        else:
            kertoma = kertoma + 1
            tulo = tulo * kertoma
        sanakirja[kertoma] = tulo

    return sanakirja

if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])