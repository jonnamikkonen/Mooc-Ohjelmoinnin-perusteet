luku = int(input("Anna luku: "))
muuttuja = 0
muuttuja1 = 0

while luku >= muuttuja:
    muuttuja1 += 1
    muuttuja += 1
    print(f"{muuttuja} X {muuttuja1} = {muuttuja*muuttuja1}")
    muuttuja1 += 1
    print(f"{muuttuja} X {muuttuja1} = {muuttuja*muuttuja1}")
    muuttuja += 1
    muuttuja1 -= 1
    print(f"{muuttuja} X {muuttuja1} = {muuttuja*muuttuja1}")
    