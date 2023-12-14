sum_of_all_numbers = 0
string = ""
number = int(input("Enter number: "))

for i in range(1, number + 1, 1):
    sum_of_all_numbers += i
    if i != number:
        string = string + str(i) + " + "
    else:
        string = string + str(i) + " = " + str(sum_of_all_numbers)

print("====")
print(string)
