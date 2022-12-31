# Kirjoita ratkaisu tähän
luku = int (input ("Anna luku: "))
i = 1
m = 2

if luku == 3:
    print(m)
    print(i)
    print(i+2)

elif luku == 1:
    print(i)

elif luku >= 2:
    print(m)
    print(i)

if luku %2 == 0:
    while i <= luku-2 or m <= luku-2:
        m += 2
        print(m)
        i += 2
        print(i)

if luku %2 != 0 and luku >4:
    while i < luku:
        if m+1 < luku:
            m += 2
            print(m)
         
        i += 2
        print(i)
        
            