def is_schrikkeljaar(jaar):
    if jaar % 4 == 0 and jaar % 100 != 0:
        antwoord = f"{jaar} is een schrikkeljaar"
    elif jaar % 400 == 0:
        antwoord = f"{jaar} is een schrikkeljaar"
    else:
        antwoord = f"{jaar} is geen schrikkeljaar"
    return antwoord


jaar = int(input("Geef een jaartal: "))
print(is_schrikkeljaar(jaar))
