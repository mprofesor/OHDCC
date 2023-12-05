# This simple program generates password using letters numbers and symbols

# Importing modules
import random

# Lists
letters = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q','r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z' 
            ]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Greeter
print("Welcome to the PyPassword Generator!")
# User input
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Password generator
#        |||
#        vvv     
password_lenght = num_letters + num_numbers + num_symbols
password = ''
for i in range(0, password_lenght):
    rand_lsn = random.randint(1, num_letters + num_symbols + num_numbers)
    if rand_lsn >= 1 and rand_lsn <= num_letters and num_letters != 0:
        password += letters[random.randint(0,len(letters)-1)]
        num_letters -= 1
    elif rand_lsn > num_letters and rand_lsn <= num_symbols + num_letters and num_symbols != 0:
        password += symbols[random.randint(0,len(symbols)-1)]
        num_symbols -= 1
    elif rand_lsn > num_letters + num_symbols and rand_lsn < num_letters + num_symbols + num_numbers and num_numbers != 0:
        password += numbers[random.randint(0,len(numbers)-1)]
        num_numbers -= 1
    elif num_letters != 0:
        password += letters[random.randint(0,len(letters)-1)]
        num_letters -= 1
    elif num_symbols != 0:
        password += symbols[random.randint(0,len(symbols)-1)]
        num_symbols -= 1
    elif num_numbers != 0:
        password += numbers[random.randint(0,len(numbers)-1)]
        num_numbers -= 1

# This is maybe not beautiful but it works. Problem is this
# might generate passwords that have strings of the same type
# of character for example 12334515 or abddfksl or ^&*($#) it
# is not checking what was before just do what can do :D
# (UPUPUP)Fixed it mostly XD


# Print output
print(f"Your random generated password: {password}")
print(len(password))
