# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, mjono):
    if len(mjono) >0:
        print(mjono[0:1]*leveys)
    elif len(mjono) == 0:
        print("*"*leveys)

def risunelio(koko):
    kerrat = koko
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    while kerrat > 0:
        x = koko
        viiva(x, "#")
        kerrat -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(3)
