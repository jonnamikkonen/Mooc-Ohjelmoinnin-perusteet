# Kirjoita ratkaisu tähän
sana = input("Sana: ")
raamit = "*" *30
lensana = (30-len(sana)-4)
keskikohta = ((lensana//2)) 
kk = (keskikohta * " ")


if len(sana) < 26:
    print(raamit)
    print("*", end = " ")
    print(kk + sana + kk, end = " ")
    if len(sana) % 2 == 0:
        print("*")
        print(raamit)
    elif len(sana) % 2 != 0:
        print(" *")
        print(raamit)
elif len(sana) >25 and len(sana) < 28:
    print(raamit)
    print("* " + sana + "*")
    print(raamit)
