def letters_tellen(woord):
    hoofdletters = 0
    kleine_letters = 0

    for char in woord:
        if char.isupper():
            hoofdletters += 1
        elif char.islower():
            kleine_letters += 1
        else:
            pass

    return [hoofdletters, kleine_letters]

zin = input("Voer een zin in: ")
resultaat = letters_tellen(zin)
print(resultaat)
print("Originele string:", zin)

print("Aantal hoofdletters:", resultaat[0])
print("Aantal kleine letters:", resultaat[1])
print("Totaal aan chars:", len(zin))
