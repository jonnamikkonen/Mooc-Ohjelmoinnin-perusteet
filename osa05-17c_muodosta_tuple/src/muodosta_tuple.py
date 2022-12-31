# tee ratkaisu tänne
def tee_tuple (x: int, y: int, z: int):
    uusi = ()
    tuple = (x, y, z)
    pienin = min(tuple)
    suurin = max(tuple)
    summa = (x+y+z)
    
    uusi = pienin, + suurin, + summa

    return uusi

if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))