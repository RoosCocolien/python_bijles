nummer = int(input('Voer een getal tussen 100 en 500 in: '))

while nummer < 100 or nummer > 500:
    print('Onjuist nummer, vul a.u.b. een geldig nummer in:')
    nummer = int(input('Voer een getal tussen 100 en 500 in: '))
else:
    print("Het gegeven nummer " + str(nummer) + " valt binnen het bereik.")
