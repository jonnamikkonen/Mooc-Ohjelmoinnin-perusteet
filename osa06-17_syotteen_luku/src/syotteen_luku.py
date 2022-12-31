# tee ratkaisu tänne
def lue(syote:str, luku1, luku2):
    while True:
        try:
            syote = input("syötä luku: ")
            luku = int(syote)
            if luku >= luku1 and luku <= luku2:
                return luku
            else:
                print(f"Syötteen on oltava kokonaisluku väliltä {luku1}...{luku2}")
        except ValueError:
            print(f"Syötteen on oltava kokonaisluku väliltä {luku1}...{luku2}")
        
if __name__ == "__main__":
    luku = lue(yks, kaks, 100)
    print("syötit luvun:", luku)