# Kirjoita ratkaisu tähän
muuttuja = -1

while muuttuja < 0:
    mjono = input("Anna merkkijono: ")
    print(mjono)
    print("-"*len(mjono))
    if len(mjono) == 0:
        break