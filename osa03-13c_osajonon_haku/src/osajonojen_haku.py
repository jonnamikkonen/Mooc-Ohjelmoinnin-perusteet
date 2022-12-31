# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")
kohta = sana.find(merkki)

if kohta <= (len(sana)-3):
    print(sana[kohta:(kohta+3)])