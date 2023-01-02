# tee ratkaisu tänne
def sarake_oikein(sudoku: list, sarake_nro: int): 
    lista = []
    käytetyt = []
    for rivi in sudoku:
        if rivi[sarake_nro] in lista and rivi[sarake_nro] != 0:
            käytetyt.append(rivi[sarake_nro])            
        else:    
            lista.append(rivi[sarake_nro]) 
        
        rivi[+1]

    if len(käytetyt) == 0:
        return True
    else:
        return False
                
if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sarake_oikein(sudoku, 0))
    print(sarake_oikein(sudoku, 1))