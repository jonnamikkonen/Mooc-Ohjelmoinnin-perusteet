# Kirjoita ratkaisu tähän
mjono = input("Anna merkkijono: ")
osajono = input("Anna osajono: ")
kohta = mjono.find(osajono,mjono.find(osajono)+len(osajono))

if kohta != -1:
    print(f"Osajonon toinen esiintymä on kohdassa {kohta}.")
else:
    print(f"Osajono ei esiinny merkkijonossa kahdesti.")