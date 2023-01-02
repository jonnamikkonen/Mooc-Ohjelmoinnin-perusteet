def rivi_oikein(sudoku: list, rivi_nro: int):
    rivi = sudoku[rivi_nro]
    for rivi_nro in sudoku:
        lista = []
        käytetyt = []
        for numero in rivi:
            if numero in lista and numero != 0:
                käytetyt.append(numero)
            else:    
                lista.append(numero)
            
        if len(käytetyt) == 0:
            return True
            break
        else:
            return False
            break
                
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

    print(rivi_oikein(sudoku, 0))
    print(rivi_oikein(sudoku, 1))