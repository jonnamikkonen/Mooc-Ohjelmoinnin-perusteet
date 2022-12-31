# Tee ratkaisu tänne
def anagrammi(mjono1, mjono2):
    j1 = sorted(mjono1)
    j2 = sorted(mjono2)
    
    if j1 == j2:
        return True
    elif j1 != j2:
        return False


if __name__ == "__main__":
    print(anagrammi("i", "a"))