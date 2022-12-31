# Kirjoita ratkaisu tähän
mjono = input("Anna merkkijono: ")
kohta = 1

while len(mjono) > kohta-1:
    print(mjono[0:kohta])
    kohta += 1