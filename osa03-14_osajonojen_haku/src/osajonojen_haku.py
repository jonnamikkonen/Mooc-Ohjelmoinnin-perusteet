# Kirjoita ratkaisu tähän
mjono = input("Sana: ")
merkki = input("Merkki: ")
kohta = mjono.find(merkki)

kohta2 = kohta+3
sana = mjono[kohta:kohta2]

while True:
    if kohta == -1 or kohta2 > len(mjono):
        break
    else:
        print(sana)
        mjono = mjono[(kohta+1):]
        kohta = mjono.find(merkki)
        kohta2 = kohta+3
        sana = mjono[kohta:kohta2]