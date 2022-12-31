# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, mjono):
    if len(mjono) >0:
        print(mjono[0:1]*leveys)
    elif len(mjono) == 0:
        print("*"*leveys)

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    kerrat = koko-koko
    x = 1
    while x <= koko:
        viiva(x, "#")
        x += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
