# tee ratkaisu tänne
def pisin(merkkijonot: list):
    pisin = max(merkkijonot, key=len)
    pisin = pisin.replace('"','')
    return pisin

if __name__ == "__main__":
    lista = ['Arto', 'Matti', 'kissa', 'koira']
    print(pisin(lista))
    