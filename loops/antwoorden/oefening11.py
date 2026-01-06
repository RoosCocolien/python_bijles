getal = int(input('Voer een getal in:'))

resultaat = getal
aantalDelingen = 0
while resultaat > 1:
    resultaat /= 2
    aantalDelingen+=1

print(f'Je kan {getal} {aantalDelingen} keer door twee delen totdat het kleiner of gelijk is aan 1.')
