# Kirjoita ratkaisu tähän
sana = input("Anna sana: ")
kirjainten_maara = len(sana)
if kirjainten_maara > 1:
    print(f"Sanassa {sana} on {kirjainten_maara} kirjainta")
if kirjainten_maara <= 1:
    print(" ")
print("Kiitos!")
