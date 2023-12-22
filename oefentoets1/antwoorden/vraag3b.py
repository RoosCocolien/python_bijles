def is_schrikkeljaar(jaar):
    if jaar % 4 == 0 and jaar % 100 != 0:
        schrikkeljaar = True
    elif jaar % 400 == 0:
        print(jaar % 400)
        schrikkeljaar = True
    elif jaar % 100 == 0:
        schrikkeljaar = False
    else:
        schrikkeljaar = False
    return schrikkeljaar


jaar = int(input("Geef een jaartal: "))
result = is_schrikkeljaar(jaar)

if result == True:
    print(f"{jaar} is een schrikkeljaar.")
else:
    print(f"{jaar} is geen schrikkeljaar.")