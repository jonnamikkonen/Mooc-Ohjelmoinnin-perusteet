# Kirjoita ratkaisu tähän
tarina = ""
vanhasana = ""

while True:
    uusisana = input("Anna sana: ")
    if uusisana == "loppu" or uusisana == vanhasana:
        break

    else:
        vanhasana = uusisana
        tarina += uusisana + " "

print(tarina)