# Kirjoita ratkaisu tähän
salasana = input("Salasana: ")

while True:
    salasana2 = input("Toista salasana: ")
    if salasana != salasana2:
        print("Ei ollut sama!")
    elif salasana == salasana2:
        break

print("Käyttäjätunnus luotu!")