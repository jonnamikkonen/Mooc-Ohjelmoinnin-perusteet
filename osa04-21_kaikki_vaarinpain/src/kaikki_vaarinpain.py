# tee ratkaisu tänne
def kaikki_vaarinpain(mjono:list):
    lista2 = []
    l = []
    for sana in mjono:
        sana = sana[::-1]
        lista2.append(sana)
    lista2.reverse()
    lista2[::-1]
    return lista2    
        
    
    

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)