def somLijsten(lijst1, lijst2):
    if len(lijst1) != len(lijst2):
        return 'Fout! Lijsten hebben niet dezelfde lengte'
    som = 0
    for i in range(len(lijst1)):
        som += abs(lijst1[i] - lijst2[i])
    return som

print(somLijsten([1,2,3], [1,4,6]))
