
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")


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

for opnro, tehtävät in nimet.items():
    if opnro in tehtavat:
        pisteet = tehtavat[opnro]
        nimi = nimet[opnro]
        nimi = nimi.strip('\n')
        
        
        print(f"{nimi} {pisteet}")