woord = input("Voor een woord/zin in die je wilt omdraaien: ")

for index in range(len(woord) -1, -1, -1):
    print(woord[index], end="")

print("\n")
