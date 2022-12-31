# Kirjoita ratkaisu tähän
asti = int(input("Mihin asti: "))

luku1 = 1
luku2 = 1
luku3 = 1
lause = " "

while luku2 < asti:
    luku1 +=1
    luku2 +=luku1
    lause += f" + {luku1}"

print(f"Laskettiin {luku3}{lause} = {luku2}")
