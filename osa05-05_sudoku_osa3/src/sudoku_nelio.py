# tee ratkaisu tänne
def nelio_oikein(sudoku: list, rivi: int, sarake: int):
    luvut = []
    for r in range(rivi, rivi+3):
        for s in range(sarake, sarake+3):
            luku = sudoku[r][s]
            if luku > 0 and luku in luvut:
                return False
            luvut.append(luku)
 
    return True

if __name__ == "__main__":
    sudoku = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # rivi 0
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # rivi 1
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # rivi 2
    [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],   # rivi 3
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # rivi 4
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # rivi 5
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # rivi 6
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # rivi 7
    [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ],   # rivi 8
    ]

    print(nelio_oikein(sudoku, 0, 3))