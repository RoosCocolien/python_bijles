def tafel(n):
    i = 1
    while i <= 10:
        print("{:>2} * {:>1} = {:>2}".format(i, n, i*n ))
        i += 1

num = int(input("Geef een getal: "))
tafel(num)
