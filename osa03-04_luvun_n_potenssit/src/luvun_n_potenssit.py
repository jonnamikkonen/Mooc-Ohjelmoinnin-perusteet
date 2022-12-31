# Kirjoita ratkaisu tähän
asti = int(input("Mihin asti: "))
kerroin = int(input("Mikä kerroin: "))
luku1 = 1
luku2 = 2

while luku1 < asti:
    print(luku1)
    luku1 = luku1*kerroin

if asti == luku1:
    print(asti)