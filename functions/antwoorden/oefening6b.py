def tafel(n):
    i = 1
    while i <= 10:
        print(f"{i} * {n} = {i * n}")
        i += 1

num = int(input("Geef een getal: "))
tafel(num)
