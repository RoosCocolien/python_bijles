import math

x1 = int(input("X-positie van coordinaat 1 (x1): "))
y1 = int(input("X-positie van coordinaat 1 (y1): "))
x2 = int(input("X-positie van coordinaat 1 (x2): "))
y2 = int(input("X-positie van coordinaat 1 (y2): "))

afstand = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Afstand tussen de coordinaten ({x1}, {y1}) en ({x2}, {y2}): {afstand: .4f}")
