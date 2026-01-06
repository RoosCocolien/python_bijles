def letters_tellen(woord):
    upper_lower = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for char in woord:
        if char.isupper():
            upper_lower["UPPER_CASE"] += 1
        elif char.islower():
            upper_lower["LOWER_CASE"] += 1
        else:
            pass

    print("Originele string : ", woord)
    print("Aantal hoofdletters : ", upper_lower["UPPER_CASE"])
    print("Aantal kleine letters : ", upper_lower["LOWER_CASE"])


letters_tellen('The quick Brown Fox')
