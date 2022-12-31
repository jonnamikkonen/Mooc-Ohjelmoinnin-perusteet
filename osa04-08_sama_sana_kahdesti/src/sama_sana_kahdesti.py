# Kirjoita ratkaisu tähän
lista = []
x = 0
while True:
    sana = input("sana: ")
    x += 1
    if sana in lista :
        x -= 1
        print(f"Annoit {x} eri sanaa")
        break
    lista.append(sana)