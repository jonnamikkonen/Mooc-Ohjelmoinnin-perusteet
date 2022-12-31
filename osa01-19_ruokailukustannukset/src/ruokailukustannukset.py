kertojen_maara = int(input("Montako kertaa viikossa syöt Unicafessa? "))
lounaan_hinta = float(input("Unicafe lounaan hinta? "))
ruokaostokset = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

print("Kustannukset keskimäärin:")
print(f"Päivässä {(lounaan_hinta*kertojen_maara/7)+(ruokaostokset/7)} euroa ")
print(f"Viikossa {(kertojen_maara*lounaan_hinta)+ruokaostokset} euroa ")