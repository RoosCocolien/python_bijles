def draai_om(woord):
    omgedraaid_woord = ""

    for letter in woord:
        omgedraaid_woord = letter + omgedraaid_woord

    return omgedraaid_woord


print(draai_om('1234abcd'))
