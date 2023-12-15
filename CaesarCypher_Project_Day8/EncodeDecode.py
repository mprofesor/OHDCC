def Encode(message, shift, alphabet_s, alphabet_l, symbols):
    # Debug
    print("Encoding")
    print(len(alphabet_s))
    
    for i in range (0, len(message)):
        if message[i] in alphabet_s:
            for j in range(0, len(alphabet_s)):
                if message[i] == alphabet_s[j]:
                    message[i] = alphabet_s[(j + shift) % len(alphabet_s)]
                    break
        elif message[i] in alphabet_l:
            for j in range(0, len(alphabet_l)):
                if message[i] == alphabet_l[j]:
                    message[i] = alphabet_l[(j + shift) % len(alphabet_l)]
                    break
        elif message[i] in symbols:
            for j in range(0, len(symbols)):
                if message[i] == symbols[j]:
                    message[i] = symbols[(j + shift) % len(symbols)]
                    break
        else:
            message[i] = message[i]

def Decode(message, shift, alphabet_s, alphabet_l, symbols):
    # Debug
    print("Decoding")

    for i in range (0, len(message)):
        if message[i] in alphabet_s:
            for j in range(0, len(alphabet_s)):
                if message[i] == alphabet_s[j]:
                    message[i] = alphabet_s[(j - shift) % len(alphabet_s)]
                    break
        elif message[i] in alphabet_l:
            for j in range(0, len(alphabet_l)):
                if message[i] == alphabet_l[j]:
                    message[i] = alphabet_l[(j - shift) % len(alphabet_l)]
                    break
        elif message[i] in symbols:
            for j in range(0, len(symbols)):
                if message[i] == symbols[j]:
                    message[i] = symbols[(j - shift) % len(symbols)]
                    break
        else:
            message[i] = message[i]
    


# Need to write functions