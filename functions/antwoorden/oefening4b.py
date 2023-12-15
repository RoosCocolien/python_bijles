def string_reverse(string):
    reversed_string = ""

    for letter in string:
        reversed_string = letter + reversed_string

    return reversed_string


print(string_reverse('1234abcd'))
