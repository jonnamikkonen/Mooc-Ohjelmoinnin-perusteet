# tee ratkaisu tänne
import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto) as tiedosto:
        data = tiedosto.read()    
    henkilot = json.loads(data)
    for henkilo in henkilot:
        harrastukset = tuple(henkilo["harrastukset"])
        
        print(henkilo["nimi"], henkilo["ika"], harrastukset)
        

if __name__ == "__main__":
    tulosta_henkilot("tiedosto1.json")

