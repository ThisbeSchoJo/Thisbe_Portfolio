#calculator that accepts input from user

import math


print("Welcome to the Calculator!\n")
while 1:
    print("What would you like to do?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square root")
    print("7. Exit calculator")
    choice = int(input("Enter your choice(1-7): "))
    if choice == 1: # add
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Output: ", num1+num2)
    elif choice == 2: #subtract
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Output: ", num1-num2)
    elif choice == 3: #multiply
        num1 = int(input("Enter first number: "))
        num2 = int(input("Multiplied by: "))
        print("Output: ", num1*num2)
    elif choice == 4: #divide
        num1 = int(input("Enter first number: "))
        num2 = int(input("Divided by: "))
        print("Output: ", num1/num2)
    elif choice == 5: #exponent
        num1 = int(input("Enter first number: "))
        num2 = int(input("Exponent: "))
        print("Output: ", num1**num2)
    elif choice == 6: #square root
        num1 = int(input("Enter number: "))
        print("Output: ", math.sqrt(num1))
    elif choice == 7: #exit
        print("Exiting calculator...")
        break
