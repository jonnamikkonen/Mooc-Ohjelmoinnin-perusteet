# Kirjoita ratkaisu tähän
sana1 = input("Anna 1. sana: ")
sana2 = input("Anna 2. sana: ")

if sana1 > sana2:
    print(f"{sana1} on aakkosjärjestyksessä viimeinen. ")
elif sana2 > sana1:
    print(f"{sana2} on aakkosjärjestyksessä viimeinen. ")
elif sana1 == sana2:
    print("Annoit saman sanan kahdesti.")