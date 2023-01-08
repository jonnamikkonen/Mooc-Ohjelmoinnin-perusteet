vuosi = int(input("Vuosi: "))
year = vuosi +1

while True:
   if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
      break
   year += 1
print(f"Vuotta {vuosi} seuraava karkausvuosi on {year}")
   


    





