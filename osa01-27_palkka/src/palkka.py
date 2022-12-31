tuntipalkka = float(input("Tuntipalkka: "))
tunnit = float(input("Työtunnit: "))
viikonpaiva = (input("Viikonpäivä: "))
if viikonpaiva != "sunnuntai":
    print(f"Palkka {tuntipalkka * tunnit} euroa")
if viikonpaiva == "sunnuntai":
    print(f"Palkka {tuntipalkka * tunnit * 2} euroa")