kleuren = ["rood", "oranje", "groen"]

kleur = input("Welke kleur heeft het verkeerslicht?: ").lower()

while True:
    if kleur not in kleuren:
        print("Deze kleur herken ik niet")
        kleur = input("Welke kleur heeft het verkeerslicht?: ").lower()
    else:
        if kleur == 'rood':
            print('Stop de auto')
            break
        elif kleur == 'oranje':
            print('Stop de auto')
            break
        elif kleur == 'groen':
            print('Je mag doorrijden')
            break
