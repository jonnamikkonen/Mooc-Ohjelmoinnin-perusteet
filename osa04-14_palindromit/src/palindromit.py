# tee ratkaisu tänne

def palindromi(mjono):
    takaperin = (mjono[::-1])
    if mjono == takaperin:
        return True
    if mjono != takaperin:
        return False
while True:
    mjono = input("Anna palindromi: ")
    takaperin = (mjono[::-1])
        
    if mjono == takaperin:
        print(f"{mjono} on palindromi!")
        break
    elif mjono != takaperin:
        print("ei ollut palindromi")

if __name__ == "__main__":
    print(palindromi("saippuakauppias"))



# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
