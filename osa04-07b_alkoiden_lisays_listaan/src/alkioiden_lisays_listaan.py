# Kirjoita ratkaisu tähän
maara = int(input("Kuinka monta lukua? "))
luvut = []
while maara > 0:
    luku1 = int(input("Anna luku 1: "))
    luvut.append(luku1)
    maara -= 1

print(luvut)