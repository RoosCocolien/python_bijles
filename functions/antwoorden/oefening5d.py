def letters_tellen(woord):
    dict_upper_lower = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for char in woord:
        if char.isupper():
            dict_upper_lower["UPPER_CASE"] += 1
        elif char.islower():
            dict_upper_lower["LOWER_CASE"] += 1
        else:
            pass

    return dict_upper_lower


zin = input("Voer een zin in: ")
result = letters_tellen(zin)
print(result)
print("Originele string:", zin)

print("Aantal hoofdletters:", result['UPPER_CASE'])
print("Aantal kleine letters:", result['LOWER_CASE'])
print("Totaal aan characters:", len(zin))