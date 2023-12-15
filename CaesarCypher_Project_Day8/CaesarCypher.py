from ASCII_ART import banner
from EncodeDecode import Encode
from EncodeDecode import Decode

# Alphabet table
alphabet_pl_s = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's',
                 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']

alphaber_pl_l = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I',
                 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S',
                 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']

special_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ';', ':',
                   '<', '>', ',', '.', '/', '?', '~', '+', '-', '=', '_', '|']

# Printing beautiful ASCII ART
print(banner)

Stop = False

while not Stop:
    # Ask for a message to input
    message = input("Please enter message: ")
    choice_function = input("Do you want to 'encrypt' or 'decrypt' message: ")
    shift = int(input("Please enter the shift(integer): "))
    message_list = []

    # Changing message string to a list
    for i in range(0, len(message)):
        message_list.append(message[i])

    if choice_function == 'encrypt':
        Encode(message_list, shift, alphabet_pl_s, alphaber_pl_l, special_symbols)
    elif choice_function == 'decrypt':
        Decode(message_list, shift, alphabet_pl_s, alphaber_pl_l, special_symbols)
    else:
        print("You chose wrong function.")

    processed_message = ""

    for letter in message_list:
        processed_message += letter

    print(f"Processed message:{processed_message}")
    choice_end = input("Do you whish to encode/decode more? ('yes'/'no')")
    if choice_end == 'no':
        Stop = True
