# tee ratkaisu tänne
sanakirja = {}
while True:
    komento = input("komento (1 hae, 2 lisää, 3 lopeta: ")
    if komento == "2":
        nimi = input("nimi: ")
        numero = input("numero: ")
        sanakirja[nimi] = numero
        print(sanakirja)
        print("ok!") 
    if komento == "1":
        nimi = input("nimi: ")
        print(sanakirja)
        if nimi not in sanakirja:
            print("ei numeroa")
        else:
            print(list(sanakirja.items()).index(numero))
    if komento == "3":
        print("lopetetaan...")
        break