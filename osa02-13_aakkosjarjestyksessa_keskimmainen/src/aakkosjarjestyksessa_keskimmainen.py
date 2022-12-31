# Kirjoita ratkaisu tähän
k1 = str(input("Anna 1. kirjain: "))
k2 = str(input("Anna 2. kirjain: "))
k3 = str(input("Anna 3. kirjain: "))
 
if k1 > k2 and k2 > k3:
    print(f"Keskimmäinen kirjain on {k2} ")
elif k2 > k3 and k3 > k1:
    print(f"Keskimmäinen kirjain on {k3} ")
elif k3 > k1 and k1 > k2:
    print(f"Keskimmäinen kirjain on {k1} ")
elif k1 > k3 and k3 > k2:
    print(f"Keskimmäinen kirjain on {k3} ")
elif k2 > k1 and k1 > k3:
    print(f"Keskimmäinen kirjain on {k1} ")
elif k3 > k2 and k2 > k1:
    print(f"Keskimmäinen kirjain on {k2} ")
