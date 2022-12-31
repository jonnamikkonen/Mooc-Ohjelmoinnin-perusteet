# Kirjoita ratkaisu tähän
lista = []
jarjes = []
while True:
    luku = int(input("Anna luku: "))
    
    if luku == 0:
        print("Moi!")
        break
    if luku != "0":
        lista.append(luku) 
        alkup = lista     
        print("Lista:", alkup)
    if luku != "0":
        jarjes.append(luku)
        jarjes.sort()
        print("Järjestettynä:", jarjes)

    