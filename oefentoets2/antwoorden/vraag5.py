def isPositiefEnKleinerDan(x, y):
    return 0 <= x < y


print(isPositiefEnKleinerDan(-19, 100))
print(isPositiefEnKleinerDan(19, 100))
print(isPositiefEnKleinerDan(100, -19))
