# tee ratkaisu tänne
def transponoi (matriisi: list):
    for rivi in matriisi:
        lista = []
        lista.append(rivi[0])
        print(" ".join(lista))
        
    for rivi in matriisi:
        print(rivi[1], end = " ")
        
        
            
if __name__ == "__main__":
    matriisi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transponoi(matriisi)