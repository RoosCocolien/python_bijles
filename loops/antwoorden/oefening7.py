naam = "Marie Antoinette van Oostenrijk"
aantal = 0
letter = 'a'
for char in naam:
    if char.lower() == letter:
        aantal += 1

print("In de naam " + naam + " komt de letter '" + letter + "' " + str(aantal) +"x voor")

