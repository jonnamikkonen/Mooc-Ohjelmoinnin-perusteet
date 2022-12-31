# tee ratkaisu tänne
def uusi_henkilo(nimi: str, ika: int):
    henkilo = ()
    henkilo = (nimi, ika)

    osat = nimi.split(" ")
    try:
        if not osat[1]:
            raise ValueError
    except IndexError:
        raise ValueError
    if len(nimi) > 40:
        raise ValueError
    if len(nimi) == 0:
        raise ValueError
    if not nimi.split(" "):
        raise ValueError
    if ika < 0:
        raise ValueError
    if ika > 150:
        raise ValueError
    
   

    return henkilo
if __name__ == "__main__":
    print(uusi_henkilo("Pekka", 50))