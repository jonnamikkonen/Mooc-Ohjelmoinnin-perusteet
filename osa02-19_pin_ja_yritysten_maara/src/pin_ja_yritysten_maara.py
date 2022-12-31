# Kirjoita ratkaisu tähän
yritykset = 0
while True:
    koodi = input("PIN-koodi: ")
    yritykset += 1

    if koodi != "4321":
        onnistui = False
        print("Väärin")
    if koodi == "4321":
        onnistui = True
        break
if onnistui and yritykset == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
elif onnistui:
    print(f"Oikein, tarvitsit {yritykset} yritystä ")
