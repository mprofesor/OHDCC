# Main Game file

import ASCII_ART as AA
import random

def Game():
    # This is only visual part
    print(AA.ART)
    print(AA.GREETINGS)
    print(AA.INSTUCTIONS)

    # Global variable
    RANDOM_NUMBER = random.randrange(0,100)

    # This is game logic part
    result = ""

    difficulty = input(AA.GAME_DIFF_TEXT)
    if difficulty == 'hard':
        attempts = 5
    else:
        attempts = 10
    
    while attempts != 0:
        print(f"You have {attempts} attempts left")
        guessed_number = int(input(AA.ROUND_TEXT))
        if guessed_number == RANDOM_NUMBER:
            result = "winner"
            break
        elif guessed_number > RANDOM_NUMBER:
            print(f"{guessed_number} is too high!")
        elif guessed_number < RANDOM_NUMBER:
            print(f"{guessed_number} is too low!")
        attempts -= 1
    
    if result == "winner":
        print(f"\n{guessed_number}{AA.WINNER}")
    else:
        print(f"You have no attempts left!")
        print(f"\n{AA.LOOSER}{RANDOM_NUMBER}")



Game()