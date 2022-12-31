
while True:
    eroteltu1 = 0
    eroteltu2 = 0
    pisteet_harjoitukset = input("Koepisteet ja harjoitusten määrä: ")
    #rivit 5-10, syötteen erottelu kahdeksi merkkijonoksi ja mjonojen muuttaminen kokonaisluvuiksi
    luvut = pisteet_harjoitukset.split(" ")
    eroteltu1 = luvut[0]
    luvut = pisteet_harjoitukset.split(" ")
    eroteltu2 = luvut[1]

    eroteltu1 = int(eroteltu1)
    eroteltu2 = int(eroteltu2)
    lista.append(eroteltu1)
    lista.append(eroteltu2)

    if pisteet_harjoitukset == "":
        print("Tilasto:")
        break
print(lista)
def keskiarvo(keskiarvo):


   

#print(eroteltu1 + eroteltu2)
#harjoitustehtävien pisteytys


#arvosanataulukko
    if pisteet >= 0 and pisteet < 15 or eroteltu1 <=10:
        arvosana 0
    elif pisteet >= 15 and pisteet <18:
        arvosana 1
    elif pisteet >= 18 and pisteet <21:
        arvosana 2
    elif pisteet >=21 and pisteet <24:
        arvosana 3
    elif pisteet >= 24 and pisteet <28:
        arvosana 4
    elif pisteet >= 28 and pisteet <=30:
        arvosana 5

    if __name__ == "__main__":
        print("Pisteiden keskiarvo", keskiarvo)
        print()