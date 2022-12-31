# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, mjono):
    if len(mjono) >0:
        print(mjono[0:1]*leveys)
    elif len(mjono) == 0:
        print("*"*leveys)

def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    while korkeus > 0:
        viiva(10, "#")
        korkeus -=1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
