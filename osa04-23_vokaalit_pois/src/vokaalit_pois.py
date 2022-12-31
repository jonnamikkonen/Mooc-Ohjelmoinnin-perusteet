# tee ratkaisu tänne
def ilman_vokaaleja(mjono):
    muuttuja = ""
    vokaalit = ("a", "e", "i", "o", "u", "y", "å", "ä", "ö" )
    for kirjain in mjono:
        if kirjain not in vokaalit:
            muuttuja = muuttuja+kirjain
    lista = muuttuja
    return lista
    
    
if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))