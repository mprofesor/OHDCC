# Greet user and print instructions to the screen
# New hand or Finish?
# Add two cards to the player's hand
# Add another card?
# Count the result and print the winner

import ASCII_ART as AA
import BlackjackFunctions as BF

import os

# Variables
InMenu = True
InGame = False

while InMenu:
    print(AA.art)
    print(AA.greet)
    menu_choice = input("Your choice(i, q, s): ")

    if menu_choice == 'i':
        os.system("clear")
        print(AA.instructions)
    elif menu_choice == 'q':
        os.system("clear")
        InMenu = False
    elif menu_choice == 's':
        os.system("clear")
        InMenu = False
        InGame = True

while InGame:
    game_deck = AA.deck_names_list

    players_hand = []
    computers_hand = []
    players_hand_value = 0
    computers_hand_value = 0
    
    # Pick two random cards from deck for the player
    players_hand = BF.Pick_random_cards(game_deck, 2)

    # Pick two random cards from deck for the computer
    computers_hand = BF.Pick_random_cards(game_deck, 2)

    while players_hand_value < 21 or computers_hand_value < 21:
        os.system("clear")
        players_hand_value = 0
        computers_hand_value = 0
        # Using functions from BlackjakFunctions.py print art and calculate results
        players_hand_value = BF.Value_the_hand(players_hand, AA.deck, players_hand_value)
        print(f"\nYour hand: {BF.Retrive_cards_art(players_hand, AA.deck)}")
        print(f"\nYour hand value: {players_hand_value}")
        
        computers_hand_value = BF.Value_the_hand(computers_hand, AA.deck, computers_hand_value)
        print(f"\nComputer's hand: {BF.Retrive_cards_art(computers_hand, AA.deck)}")
        print(f"\n Computer's hand value: {computers_hand_value}")
    
        if computers_hand_value > 21:
            break
        elif players_hand_value > 21:
            break

        ingame_choice = input("Do you wish to add another card to the hand?('y','n'): ")
        if ingame_choice == 'y':
            players_hand.append(BF.Pick_random_cards(game_deck, 1))
            if computers_hand_value <= 15 or computers_hand_value < players_hand_value and players_hand_value <= 21:
                computers_hand.append(BF.Pick_random_cards(game_deck, 1))
        else:
            if computers_hand_value <= 15 or computers_hand_value < players_hand_value and players_hand_value <= 21:
                computers_hand.append(BF.Pick_random_cards(game_deck, 1))
            else:
                break
            
    print()
    if computers_hand_value <= 21 and players_hand_value <= 21 and computers_hand_value > players_hand_value:
        print("YOU LOSE!")
    elif players_hand_value <= 21 and computers_hand_value <= 21 and computers_hand_value < players_hand_value:
        print("YOU WIN!")
    elif 21 < players_hand_value and computers_hand_value <= 21:
        print("YOU LOSE!")
    elif players_hand_value > 21 and computers_hand_value > 21:
        print("TIE!")
    elif 21 < computers_hand_value and players_hand_value <= 21:
        print("YOU WIN!")
    elif computers_hand_value == players_hand_value:
        print("YOU WIN!")
    else:
        print("I don't know how this happened!?!")

    aftergame_choice = input("\nDo you wish to QUIT('q') or START('s') another game?: ")

    if aftergame_choice == 'q':
        InGame = False
        os.system("clear")
    else:
        os.system("clear")



    





    
    


    


