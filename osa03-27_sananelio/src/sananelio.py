# tee ratkaisu tänne
def nelio(sana, maara):
    i = 0
    for line in range(maara):
        for char in range(maara):
            print(sana[i % len(sana)], end="")
            i += 1
        print()

if __name__ == "__main__":
    nelio("kissa", 4)
    print()