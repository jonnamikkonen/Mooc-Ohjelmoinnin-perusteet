print("Kerro huominen sääennuste: ")
lampotila = int(input("Lämpötila: "))
sade = input("Sataako (kyllä/ei): ")

print("Pue housut ja t-paita")
if lampotila <= 20 >= 10:
    print("Ota myös pitkähihainen paita")
if lampotila <=10 >= 5:
    print("Pue päälle takki")
if lampotila <= 5:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if sade == "ei":
    print(" ")
if sade == "kyllä":
    print("Muista sateenvarjo!")