# tee ratkaisu tänne
def lue_hedelmat ():
    sanakirja = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(";")
            sanakirja[osat[0]] = float(osat[1])
                
    return sanakirja

if __name__ == "__main__":
    print(lue_hedelmat())