num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

def optellen():
    tot = num1 + num2
    print(f"{num1} + {num2} = {tot}")

def aftrekken():
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub}")

def vermenigvuldigen():
    mul = num1 * num2
    print(f"{num1} x {num2} = {mul}")

def delen():
    div = num1 / num2
    print(f"{num1} / {num2} = {div}")

operatie = input("Welke bewerking moet er gedaan worden (+, -, *, /): ")

if operatie == "+":
    optellen()
elif operatie == "-":
    aftrekken()
elif operatie == "*":
    vermenigvuldigen()
elif operatie == "/":
    delen()
else:
    print(f"No operation for {operatie} for now! sorry!")
