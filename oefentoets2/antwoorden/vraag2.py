resultaat = 1

while True:
    getal = input("Voer een getal in: ")
    if getal == 'stop':
        break
    resultaat *= int(getal)

print(f"Als je deze getallen vermenigvuldig, is het resultaat: {resultaat}")
