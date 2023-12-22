# Python programma om te controleren of
# een string een palindroom is of niet

woord = input("Geef een woord: ")

# Draai het woord om en sla het op
# we kunnen start en eind weglaten want we willen de hele string meenemen
# derde getal geeft de stap aan
achterstevoren = woord[::-1]

if woord == achterstevoren:
    print(f"{woord} is een palindroom")
else:
    print(f"{woord} is geen palindroom")
