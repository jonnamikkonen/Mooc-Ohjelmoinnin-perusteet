def ensimmainen(merkkijono):
    sanat = merkkijono.split(" ")
    for word in sanat:
        print(word[0:1])
#     kirjoita funktion koodi tähän
# 
# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    ensimmainen('python')
    ensimmainen('yhtälö')
    ensimmainen('tieto')
    ensimmainen('huominen')
    ensimmainen('omena')
    ensimmainen('nukkumaanmenoaika')