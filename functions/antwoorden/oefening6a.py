def toon_tafel(n):
    i = 1
    while i <= 10:
        print( i, "*", n, "=", i*n )
        i += 1

num = int(input("Geef een getal: "))
toon_tafel(num)
