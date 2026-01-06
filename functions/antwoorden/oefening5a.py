def letters_tellen(woord):
    kleine_letters = 0
    hoofdletters = 0

    for char in woord:
        if char.isupper():
            hoofdletters += 1
        elif char.islower():
            kleine_letters += 1
        else:
            pass

    return [hoofdletters, kleine_letters]

woord = 'The quick Brown Fox'
resultaat = letters_tellen(woord)
print(resultaat)
print("Originele string:", woord)

print("Aantal hoofdletters:", resultaat[0])
print("Aantal kleine letters:", resultaat[1])
print("Totaal aan characters:", len(woord))