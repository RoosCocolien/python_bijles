def is_schrikkeljaar(jaar):
    if jaar % 4 == 0 and jaar % 100 != 0:
        schrikkeljaar = True
    elif jaar % 400 == 0:
        schrikkeljaar = True
    elif jaar % 100 == 0:
        schrikkeljaar = False
    else:
        schrikkeljaar = False
    return schrikkeljaar

print('Type "stop" of "exit" om het programma te be-eindigen')

while True:
    jaar = input("Geef een jaartal: ")
    if jaar == 'stop' or jaar == 'exit':
        break
    result = is_schrikkeljaar(int(jaar))
    if result:
        print(f"{jaar} is een schrikkeljaar.")
    else:
        print(f"{jaar} is geen schrikkeljaar.")
