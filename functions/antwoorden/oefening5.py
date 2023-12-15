def string_test(string):
    dict_upper_lower = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for char in string:
        if char.isupper():
            dict_upper_lower["UPPER_CASE"] += 1
        elif char.islower():
            dict_upper_lower["LOWER_CASE"] += 1
        else:
            pass

    print("Originele string : ", string)
    print("Aantal hoofdletters : ", dict_upper_lower["UPPER_CASE"])
    print("Aantal kleine letters : ", dict_upper_lower["LOWER_CASE"])


string_test('The quick Brown Fox')
