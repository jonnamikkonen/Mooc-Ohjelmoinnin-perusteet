# tee ratkaisu tänne
from random import randint

def lottonumerot(maara: int, alaraja: int, ylaraja:int):
    rivi = []
    while len(rivi) < maara:
        uusi = randint(alaraja, ylaraja)
        if uusi not in rivi:
            rivi.append(uusi)
    return sorted(rivi)

if __name__ == "__main__":
    print(lottonumerot(7, 1, 40))