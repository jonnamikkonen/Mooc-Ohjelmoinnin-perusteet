# Kirjoita ratkaisu tähän
merkkijono = input("Anna merkkijono: ")
kohta = 0

while kohta <= len(merkkijono):
    kohta -=1
    print(merkkijono[kohta])
    if merkkijono[:0]:
        break

    