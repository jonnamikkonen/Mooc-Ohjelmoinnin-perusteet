# tee ratkaisu tänne
import math
def hypotenuusa (kateetti1:float, kateetti2: float):
    tulos = math.pow(kateetti1, 2) + math.pow(kateetti2, 2)

    return math.sqrt(tulos)

if __name__ == "__main__":
    print(hypotenuusa(3.0, 4.0))