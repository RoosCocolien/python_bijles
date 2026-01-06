def letters_tellen(woord):
    upper_lower = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for char in woord:
        if char.isupper():
            upper_lower["UPPER_CASE"] += 1
        elif char.islower():
            upper_lower["LOWER_CASE"] += 1
        else:
            pass

    return upper_lower


zin = input("Voer een zin in: ")
resultaat = letters_tellen(zin)
print(resultaat)
print("Originele string:", zin)

print("Aantal hoofdletters:", resultaat['UPPER_CASE'])
print("Aantal kleine letters:", resultaat['LOWER_CASE'])
