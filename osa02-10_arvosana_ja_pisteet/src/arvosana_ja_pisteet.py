# Kirjoita ratkaisu tähän
pisteet = int(input("Anna pisteet [0-100]: "))

if pisteet <0:
    print("Arvosana: mahdotonta!")
elif pisteet >= 0 and pisteet < 50:
    print("Arvosana: hylätty")
elif pisteet >= 50 and pisteet <60:
    print("Arvosana: 1")
elif pisteet >= 60 and pisteet <70:
    print("Arvosana: 2")
elif pisteet >=70 and pisteet <80:
    print("Arvosana: 3")
elif pisteet >= 80 and pisteet <90:
    print("Arvosana: 4")
elif pisteet >= 90 and pisteet <=100:
    print("Arvosana: 5")
elif pisteet >100:
    print("Arvosana: mahdotonta! ")
   