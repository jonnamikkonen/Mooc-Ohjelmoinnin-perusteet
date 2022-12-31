# Kirjoita ratkaisu tähän
tulo = 1
i = 1

while True:
    luku = int(input("Anna luku: "))

    if luku <= 0 :
        print("Kiitos ja moi!")
        break

    tulo = 1
    i = 1
    while luku+1 >= i:
        tulo *= i
        i += 1
        if luku+1 == i:
            print(f"Luvun {luku} kertoma on {tulo}")

    

            