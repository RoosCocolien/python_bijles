def string_test(string):
    upper_case = 0
    lower_case = 0

    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        else:
            pass

    return [upper_case, lower_case]

string = input("Voer een zin in: ")
result = string_test(string)
print(result)
print("Originele string:", string)

print("Aantal hoofdletters:", result[0])
print("Aantal kleine letters:", result[1])
print("Totaal aan characters:", len(string))
