def vermenigvuldigen(nummers):
    totaal = 1
    for x in nummers:
        totaal *= x
    return totaal

print(vermenigvuldigen((8, 2, 3, -1, 7)))
