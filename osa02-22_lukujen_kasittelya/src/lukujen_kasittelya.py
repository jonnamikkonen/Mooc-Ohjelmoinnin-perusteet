# Kirjoita ratkaisu tähän
yritykset = 0
summa = 0
keskiarvo = 0
posi = 0
nega = 0

while True:
    luku = int(input("Syötä kokonaislukuja, 0 lopettaa: "))
   
    yritykset += 1
    if luku == 0:
        break
    summa += luku
    keskiarvo = summa/yritykset
    if luku > 0:
        posi += 1
    elif luku <0:
        nega += 1

print("Syötä kokonaislukuja, 0 lopettaa: ")
print(f"Lukuja yhteensä {yritykset-1}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {keskiarvo} ")
print(f"Positiivisia {posi}")
print(f"Negatiivisia {nega}")