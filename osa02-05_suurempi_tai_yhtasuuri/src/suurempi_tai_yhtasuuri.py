# Kirjoita ratkaisu tähän
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku:"))

if luku1 > luku2:
    print(f"Suurempi luku: {luku1} ")
elif luku2 > luku1:
    print(f"Suurempi luku: {luku2} ")
elif luku1 == luku2:
    print("Luvut ovat yhtä suuret!")
