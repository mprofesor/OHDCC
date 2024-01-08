# This is main file of Text Based Calculator
import ASCII_ART
import CalculateFunctions as CF
import os

# Print ASCII ART
print(ASCII_ART.Greeting)

# Print some instructions
print("Hello and welcome to the Simple Text Based Calculator")
print("To start calculate input numbers and then choice what to do with them.")
print("Every calculation is done in such a way: (FirstNumber <operator> SecondNumber).")
print("If you choose to continue ongoing calculations you will be able to input just SecondNumber.\n")

# Variables
Calculate = True
number_calculated = 0

while Calculate:
    # Take input from the user
    if number_calculated == 0:
        number1 = float(input("First Number: "))
    else:
        number1 = number_calculated
    number2 = float(input("Second Number: "))
    operation = input("\nOperation: \n'+' - Add\n'-' - Subtract\n'*' - Multiply\n'/' - Divide\n: ")

    if operation == '+':
        number_calculated = CF.Add(number1, number2)
    elif operation == '-':
        number_calculated = CF.Subtract(number1, number2)
    elif operation == '*':
        number_calculated = CF.Multiply(number1, number2)
    elif operation == '/':
        if number2 != 0:
            number_calculated = CF.Divide(number1, number2)
        else:
            print("INFINITY")
    else:
        print("You chose not exesting operation!")

    print(f"{number1} {operation} {number2} = {number_calculated}")

    choice = input("Do you wish to CONTINUE(c), START NEW CALC(n) or QUIT(q): ")

    if choice == 'n':
        number_calculated = 0
        os.system("clear")
    elif choice == 'q':
        Calculate = False
    elif choice == 'c':
        os.system("clear")
        print(number_calculated)
    else:
        os.system("clear")

