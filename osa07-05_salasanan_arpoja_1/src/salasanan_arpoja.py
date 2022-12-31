# tee ratkaisu tänne
import string
from random import *
def luo_salasana(pituus: int):
    kirjaimet = string.ascii_lowercase
    return choice(kirjaimet)


if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(4))