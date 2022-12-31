# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(leveys, mjono):
    if len(mjono) >0:
        print(mjono[0:1]*leveys)
    elif len(mjono) == 0:
        print("*"*leveys)
def kuvio(koko1, kolmio, koko2, nelio):
    kerrat = koko1-koko1
    kerrat2 = koko2
    x = 1
    while x <= koko1:
        viiva(x, kolmio)
        x += 1
    while kerrat2 > 0:
        viiva(koko1, nelio)
        kerrat2 -=1
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "x", 3, "*")