# tee ratkaisu tänne
nimi = input("Kenelle teos omistetaan: ")
paikka = input("Mihin kirjoitetaan: ")

with open (paikka, "w") as tiedosto:
    tiedosto.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")