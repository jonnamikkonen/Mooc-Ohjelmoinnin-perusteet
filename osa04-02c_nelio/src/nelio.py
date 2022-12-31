# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, mjono):
    if len(mjono) >0:
        print(mjono[0:1]*leveys)
    elif len(mjono) == 0:
        print("*"*leveys)

def nelio(koko, merkki):
    kerrat = koko
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    while kerrat > 0:
        x = koko
        viiva(koko, merkki)
        kerrat -=1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "+")
