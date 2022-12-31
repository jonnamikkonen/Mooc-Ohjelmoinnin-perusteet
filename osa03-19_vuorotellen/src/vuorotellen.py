# Kirjoita ratkaisu tähän
luku = int(input("Anna luku: "))
i = 1

if luku %2 == 0: #parilliset
    while i < luku:
        print(i)
        i += 1
        print(luku)
        luku -= 1

if luku %2 != 0: #parittomat
    while i-1 < luku:
        print(i)
        i += 1
        if luku+1 != i:
            print(luku)
            luku -= 1