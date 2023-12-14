nummers = [10, 20, 30, 40, 50]

som = 0
for nummer in nummers:
    som = som + nummer

lijst_lengte = len(nummers)
gemiddelde = som / lijst_lengte
print("Het gemiddelde is: " + str(gemiddelde))