def string_reverse(string):

    reversed_string = ''
    index = len(string)

    while index > 0:
        reversed_string += string[ index - 1 ]
        index = index - 1
    return reversed_string

print(string_reverse('1234abcd'))

