# Kirjoita ratkaisu tähän
sana = input("Sana: ")
lensana = 20-len(sana)

if len(sana) < 21:
    print("*"*lensana + sana)
    