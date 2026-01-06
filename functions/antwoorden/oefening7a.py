def aantal_letters_gemeen(woord1,woord2):
    tekens = []
    for letter in woord1:
        if (letter in woord2) and (letter not in tekens):
            tekens += letter
    return len(tekens)

input1 = input("Geef woord 1: ")
input2 = input("Geef woord 2: ")

num = aantal_letters_gemeen(input1, input2)

if num <= 0:
    print( "De woorden delen geen tekens." )
elif num == 1:
    print( "De woorden hebben 1 teken gemeen" )
else:
    print( "De woorden hebben", num, "tekens gemeen" )
