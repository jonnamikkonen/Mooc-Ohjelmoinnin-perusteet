# tee ratkaisu tänne
def suodata_laskut():
    with open ("laskut.csv") as tiedosto:
        sisalto = tiedosto.read()
        for rivi in tiedosto:
            osat = rivi.split(';')

            if osat[1]-osat[2] == osat[3]:
                with open ("oikeat.csv", "w") as tiedosto1:
                    tiedosto1.write(osat)

            if osat[1]+osat[2] == osat[3]:
                with open ("oikeat.csv", "w") as tiedosto1:
                    tiedosto1.write(osat)
            
            if osat[1]-osat[2] != osat[3]:
                with open ("vaarat.csv", "w") as tiedosto2:
                    tiedosto2.write(osat)
            
            if osat[1]+osat[2] != osat[3]:
                with open ("vaarat.csv", "w") as tiedosto2:
                    tiedosto2.write(osat)

if __name__ == "__main__":
    print(suodata_laskut())