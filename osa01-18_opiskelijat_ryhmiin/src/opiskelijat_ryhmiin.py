opiskelijoiden_maara = int(input("Montako opiskelijaa? "))
ryhman_koko = int(input("Mikä on ryhmän koko? "))

print(f"Ryhmien määrä: {(opiskelijoiden_maara+ryhman_koko-1) // ryhman_koko}")
