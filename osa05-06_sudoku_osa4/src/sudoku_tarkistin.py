# tee ratkaisu tänne
def sarake_oikein(sudoku: list, sarake: int):
    luvut = []
    for rivi in sudoku:
        luku = rivi[sarake]
        if luku > 0 and luku in luvut:
            False
        luvut.append(luku)
 
    sarake_oikein = True

def rivi_oikein(sudoku: list, rivi: int):
    luvut = []
    for luku in sudoku[rivi]:
        if luku > 0 and luku in luvut:
            False
        luvut.append(luku)
 
    rivi_oikein = True

def nelio_oikein(sudoku: list, rivi: int, sarake: int):
    luvut = []
    for r in range(rivi, rivi+3):
        for s in range(sarake, sarake+3):
            luku = sudoku[r][s]
            if luku > 0 and luku in luvut:
                False
            luvut.append(luku)
 
    nelio_oikein = True

def sudoku_oikein(sudoku1: list):
    if rivi_oikein == True and sarake_oikein == True and nelio_oikein == True:
        return True
    else:
        return False

if __name__ == "__ main__":
    rivi_oikein(sudoku1, 0)
    sarake_oikein(sudoku1, 0)
    nelio_oikein(sudoku1, 3, 3)
    sudoku1 = [
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

    print(sudoku_oikein(sudoku1))