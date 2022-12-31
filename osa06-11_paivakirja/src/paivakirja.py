# tee ratkaisu tänne
with open("paivakirja.txt", "a") as tiedosto:
    while True:
        print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
        valinta = input("Valinta: ")

        if valinta == "1":
            merkinta = input("Anna merkintä: ")
            tiedosto.write(f"{merkinta}\n")
            print("Päiväkirja tallennettu\n")

        if valinta == "2":
            print("Merkinnät: ")
            with open ("paivakirja.txt") as tiedosto:
                sisalto = tiedosto.read()
                print(sisalto)

        if valinta == "0":
            print("Heippa!")
            break