# Python programma om te controleren of
# een string een palindroom is of niet

woord = input("Geef een woord: ")

# Draai het woord om en sla het op
achterstevoren = ""
for letter in woord:
    achterstevoren = letter + achterstevoren

if woord == achterstevoren:
    print(f"{woord} is een palindroom")
else:
    print(f"{woord} is geen palindroom")
