# Calculator Angela's Version
from ASCII_ART import Greeting
from os import system

def Add(n1, n2):
    """This function adds two numbers n1 and n2"""
    return n1 + n2

def Subtract(n1, n2):
    """This function subtracts two numbers n1 and n2"""
    return n1 - n2

def Multiply(n1, n2):
    """This function multiplies two numbers n1 and n2"""
    return n1 * n2

def Divide(n1, n2):
    """This function divides two numbers n1 and n2"""
    return n1 / n2

# Using dictionary to connect symbols(keys) with function(values)
# (This is quite smart way - I have to admit that)
operations = {
    "+": Add,
    "-": Subtract,
    "*": Multiply,
    "/": Divide,
}

def Calculator():
    # Print logo
    print(Greeting)

    # Get the first number
    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        # Print out all the operations possible
        for symbol in operations:
            print(symbol)

        # Get the operation to work with
        operation_symbol = input("Pick an operation from the line above: ")
        chosen_operation = operations[operation_symbol]

        # Get the second number
        num2 = float(input("What's the next number?: "))

        # Calculate the answer using chosen operation
        answer = chosen_operation(num1, num2)

        # Print out the answer
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Print choice message:
        choice = input(f"If you want to\nContinue with an {answer} type 'c'\nStart new calculation type 'n'\nFinish calculations type 'q'\nChoice: ")
        if choice == 'c':
            num1 = answer
            system("clear")
            print(answer)
        elif choice == 'n':
            system("clear")
            # Using RECURSION here *.* NICE
            Calculator()
        elif choice == 'q':
            should_continue = False
        else:
            print("Your choice is not recognized quitting...")
            should_continue = False

Calculator()
