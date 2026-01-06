def draai_om(woord):

    woord_omgedraaid = ''
    index = len(woord)

    while index > 0:
        woord_omgedraaid += woord[ index - 1 ]
        index = index - 1
    return woord_omgedraaid

print(draai_om('1234abcd'))
