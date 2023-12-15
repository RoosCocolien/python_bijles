def string_test(string):
    dict_upper_lower = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for char in string:
        if char.isupper():
            dict_upper_lower["UPPER_CASE"] += 1
        elif char.islower():
            dict_upper_lower["LOWER_CASE"] += 1
        else:
            pass

    return dict_upper_lower


string = input("Voer een zin in: ")
result = string_test(string)
print(result)
print("Originele string:", string)

print("Aantal hoofdletters:", result['UPPER_CASE'])
print("Aantal kleine letters:", result['LOWER_CASE'])
print("Totaal aan characters:", len(string))