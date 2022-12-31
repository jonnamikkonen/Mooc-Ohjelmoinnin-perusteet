# Kirjoita ratkaisu tähän
print("Lista on nyt []")
lista = []
x = 0
while True:
    lisäys = input("(l)isää, (p)oista vai e(x)it: ")
    if lisäys == "l":
        x +=1
        lista.append(x)
        print("Lista on nyt", lista)
    if lisäys == "p":
        x -=1
        lista.pop(x)
        print("Lista on nyt", lista)
    if lisäys == "x":
        print("Moi!")
        break
    