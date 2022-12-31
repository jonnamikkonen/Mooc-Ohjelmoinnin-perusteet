opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")


nimet = {}
with open (opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        rivi = rivi.rstrip('\n')
        if osat[0]  == "opnro":
            continue
        nimet[osat[0]] = (f"{osat[1]} {osat[2]}")
     

tehtavat = {}
with open (tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        rivi = rivi.rstrip('\n')
        if osat[0] == "opnro":
            continue
        tehtavat[osat[0]] = int(osat[1]) + int(osat[2]) + int(osat[3]) + int(osat[4]) + int(osat[5]) + int(osat[6]) + int(osat[7])

koe = {}
with open (koepisteet) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == "opnro":
            continue
        koe[osat[0]] = int(osat[1]) + int(osat[2]) + int(osat[3])

for opnro, tehtävät in nimet.items():
    if opnro in tehtavat:
        pisteet = tehtavat[opnro]
        nimi = nimet[opnro]
        nimi = nimi.strip('\n')
        kpisteet = koe[opnro]
        if pisteet >= 0 and pisteet <= 3:
            uudetpisteet = 0
        if pisteet >= 4 and pisteet <= 7:
            uudetpisteet = 1
        if pisteet >= 8 and pisteet <= 11:
            uudetpisteet = 2
        if pisteet >= 12 and pisteet <= 15:
            uudetpisteet = 3
        if pisteet >= 16 and pisteet <= 19:
            uudetpisteet = 4
        if pisteet >= 20 and pisteet <= 23:
            uudetpisteet = 5
        if pisteet >= 24 and pisteet <= 27:
            uudetpisteet = 6
        if pisteet >= 28 and pisteet <= 31:
            uudetpisteet = 7
        if pisteet >= 32 and pisteet <= 35:
            uudetpisteet = 8
        if pisteet >= 36 and pisteet <= 39:
            uudetpisteet = 9
        if pisteet >= 40:
            uudetpisteet = 10
            
        koepisteet = kpisteet + uudetpisteet

        if koepisteet >= 0 and koepisteet <= 14:
            arvosana = 0
        if koepisteet >= 15 and koepisteet <= 17:
            arvosana = 1
        if koepisteet >= 18 and koepisteet <= 20:
            arvosana = 2
        if koepisteet >= 21 and koepisteet <= 23:
            arvosana = 3
        if koepisteet >= 24 and koepisteet <= 27:
            arvosana = 4
        if koepisteet >= 28:
            arvosana = 5

        print(f"{nimi} {arvosana}")


