# tee ratkaisu tänne
def histogrammi(mjono: str):
    kirjaimet = {}

    for kirjain in mjono:
        if kirjain not in kirjaimet:
            kirjaimet[kirjain] = "*"
        else:
            kirjaimet[kirjain] += "*"    
    for avain, arvo in kirjaimet.items():
        print(avain, arvo)
        

if __name__ == "__main__":
    h = histogrammi("saippuakauppias")
    
    
