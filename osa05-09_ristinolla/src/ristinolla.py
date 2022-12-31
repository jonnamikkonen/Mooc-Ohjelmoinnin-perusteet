# tee ratkaisu tänne
def pelaa_siirto(lauta: list, x: int, y: int, nappula:str):
    # "" = tyhjä ruutu
    # X = pelaajan 1 merkki
    # O = pelaajan 2 merkki
    
    for i in lauta:
        if y < 0 or y > 2 or x < 0 or x > 2:
            return False
            
        rivi = lauta[y]
        if y >= 0 and y <= 2 and x >= 0 and x <= 2 and rivi[x] == '':
            rivi[x] = nappula
            return True
        if y >= 0 and y <= 2 and x >= 0 and x <= 2 and rivi[x] == "X" or "O": 
            return False
        
if __name__ == "__main__":
    lauta = [['', 'O', 'O'], ['O', '', 'X'], ['X', '', '']]
    print(pelaa_siirto(lauta, 1, 11, "O"))
    print(lauta)