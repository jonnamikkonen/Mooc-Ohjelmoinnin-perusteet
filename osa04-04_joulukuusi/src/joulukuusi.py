# tee ratkaisu tänne
def viiva(leveys, mjono):
    if len(mjono) >0:
        print(mjono[0:1]*leveys)
    elif len(mjono) == 0:
        print("*"*leveys)

def joulukuusi(koko):
    print("joulukuusi!")
    kerrat = koko-koko
    vali = " "
    x = 1
    vkoko= koko-1
    while x <= koko*2:
        print(" "*vkoko, end="")
        viiva(x, "*")
        x += 2
        vkoko -=1
    jkoko= koko-2
    print(" "*jkoko,"*"," "*jkoko)   

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)