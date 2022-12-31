fah = int(input("Anna lämpötila (F): "))
cel = (fah - 32)/ 1.8
print(f"{fah} fahrenheit-astetta on {cel} celsius-astetta")
if cel < 0:
    print("Paleltaa!")
