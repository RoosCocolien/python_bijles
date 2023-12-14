rij_aantal = int(input("Geef een getal: "))

print("Nummer patroon ")
for i in range(1, rij_aantal + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")
