# tee ratkaisu tänne
from datetime import datetime, date

paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))
syntymapaiva = datetime(vuosi, kuukausi, paiva)

viimeinen_paiva = datetime(1999, 12, 31)

if viimeinen_paiva > syntymapaiva:
    ero = viimeinen_paiva - syntymapaiva
    print("Olit", ero.days, "päivää vanha, kun vuosituhat vaihtui.")
if viimeinen_paiva < syntymapaiva:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")