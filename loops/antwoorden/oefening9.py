getal = input('Voer een getal in:')
som = 0
while getal != 'stop':
    som += int(getal)
    print(f'De som tot nu toe is {som}')
    getal = input('Voer een getal in:')
print('Doei!')
