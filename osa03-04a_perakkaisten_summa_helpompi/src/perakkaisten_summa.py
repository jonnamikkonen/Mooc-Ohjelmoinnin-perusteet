# Kirjoita ratkaisu tähän
asti = int(input("Asti: "))

luku1 = 1
luku2 = 1

while luku2 < asti:
    luku1 +=1
    luku2 +=luku1
    
print(luku2)