# tee ratkaisu tänne
def lue_hedelmat ():
    sanakirja = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace(";", ":")
            rivi = rivi.replace("\n", "")
            osat = rivi.split(":")
            hedelma = osat[0]
            hinta = osat[1:]
            sanakirja[hedelma] = hinta

            for x in hinta:
                
    return sanakirja

if __name__ == "__main__":
    print(lue_hedelmat())