# Main Game file
import ASCII_ART as AA
import random
import DataHigherLowerGame as GD
import FunctionsHigherLowerGame as GF
import os

# Main Game function
def Game():
    # Important variables
    score = 0

    # Print some beautiful ASCII ART
    print(AA.ART)
    print("\nWelcome to the Higher Lower Game.\n")
    print("You will be asked about Instagram Accounts and their number of followers.")

    # Choice if player want to play or quit
    play_game = input("If you wish to start the game - write: 's': ")
    if play_game == 's':
        GameOver = False
    else:
        GameOver = True

    # Selecting two random numbers
    accountA = random.randint(0,19)
    accountB = random.randint(0,19)

    os.system("clear")
    # Main Game loop
    while not GameOver:
        # Print some beautiful ASCII ART
        print(AA.ART)
        # Printing score
        print(f"\nYour score: {score}\n")
        # Making sure that the numbers are not the same
        if accountA != accountB:
            # Account A data
            nameA = GF.ReturnName(GD.DATA, accountA)
            countryA = GF.ReturnCountry(GD.DATA, accountA)
            descriptionA = GF.ReturnDescription(GD.DATA, accountA)
            followersA = GF.ReturnFollowerCount(GD.DATA, accountA)

            # Account B data
            nameB = GF.ReturnName(GD.DATA, accountB)
            countryB = GF.ReturnCountry(GD.DATA, accountB)
            descriptionB = GF.ReturnDescription(GD.DATA, accountB)
            followersB = GF.ReturnFollowerCount(GD.DATA, accountB)

            # Print A VS B
            print(GF.PrintAccount(nameA, countryA, descriptionA, "A"))
            print(AA.VS)
            print(GF.PrintAccount(nameB, countryB, descriptionB, "B"))
            
            # Player input game choice
            player_guess = input("Who has more followers 'A' or 'B'?: ")

            if player_guess == 'A' and followersA > followersB:
                score += 1
                accountA = random.randint(0,19)
                accountB = random.randint(0,19)
            elif player_guess == 'B' and followersB > followersA:
                score += 1
                accountA = random.randint(0,19)
                accountB = random.randint(0,19)
            else:
                if followersA > followersB:
                    print(f"You were wrong! {nameA} has {followersA} followers which is more than {nameB} with {followersB}.")
                else:
                    print(f"You were wrong! {nameB} has {followersB} followers which is more than {nameA} with {followersA}.")
                print(f"Your score: {score}")
                end_or_not = input("Do you wish to play again?(y/n): ")
                if end_or_not == 'n':
                    GameOver = True
                else:
                    os.system("clear")
                    Game()
        else:
            accountB = random.randint(0,19)
        os.system("clear")
Game()

