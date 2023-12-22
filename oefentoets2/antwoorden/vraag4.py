woord = input("Voer een string in: ")

# oplossing  complex
omgekeerd_woord = ""
for seq in range(len(woord) - 1, -1, -1):
    # print(seq)
    omgekeerd_woord += woord[seq]

# achterstevoren = woord[::-1]
# oplossing simpel
omgekeerd = ""
for char in woord:
    omgekeerd = char + omgekeerd

print(f"Deze string omgekeerd is: {omgekeerd_woord}")
print(f"Deze string omgekeerd is: {omgekeerd}")
