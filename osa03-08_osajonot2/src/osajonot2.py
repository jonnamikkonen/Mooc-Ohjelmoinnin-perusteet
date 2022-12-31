# Kirjoita ratkaisu tähän
mjono = input("Anna merkkijono: ")
kohta = 0

while kohta > -len(mjono):
    kohta -= 1
    print(mjono[kohta:])