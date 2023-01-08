luku = int(input("Anna luku: "))
muuttuja = 1

while luku >= muuttuja:
    muuttuja1 = 1
    while muuttuja1 <= luku:
        print(f"{muuttuja} x {muuttuja1} = {muuttuja*muuttuja1}")
        muuttuja1 += 1
    muuttuja += 1
    