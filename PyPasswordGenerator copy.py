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
picked_letters = []
for l in range(1, num_letters + 1):
    picked_letters.append(random.choice(letters))

picked_symbols = []
for s in range(1, num_symbols + 1):
    picked_symbols.append(random.choice(symbols))

picked_numbers = []
for n in range(1, num_numbers + 1):
    picked_numbers.append(random.choice(numbers))

all = picked_letters + picked_numbers + picked_symbols
random.shuffle(all)
password = "".join(all)

# Print output
print(f"Your random generated password: {password}")