pisteet = int(input("Kuinka paljon pisteitä? "))

if pisteet < 100:
    pisteet1 = pisteet * 1.1

    print("Sait 10 % bonusta")
    print("Pisteitä on nyt", pisteet1)

if pisteet >= 100:
    pisteet2 = pisteet * 1.15
    print("Sait 15 % bonusta")
    print("Pisteitä on nyt", pisteet2)