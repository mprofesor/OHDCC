import ASCII_ART as AA
import BlackjackFunctions as BF

import os

# Variables
InMenu = True
InGame = False

while InMenu:
    os.system("clear")
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
    deals = 1
    
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
        
        if deals == 1:
            print(f"\nDealer's hand: {BF.Retrive_firstround_dealers_hand_art(computers_hand, AA.deck)}")
            computers_hand_value = BF.Value_firstround_dealers_hand(computers_hand, AA.deck, computers_hand_value)
        else:
            print(f"\nDealer's hand: {BF.Retrive_cards_art(computers_hand, AA.deck)}")
            computers_hand_value = BF.Value_the_hand(computers_hand, AA.deck, computers_hand_value)
        print(f"\nDealer's hand value: {computers_hand_value}")
    
        if computers_hand_value > 21:
            break
        elif players_hand_value > 21:
            break
        
        if players_hand_value < 21:
            ingame_choice = input("Do you wish to hit another card to the hand?('y','n'): ")
        if ingame_choice == 'y':
            players_hand.append(BF.Pick_random_cards(game_deck, 1))
        else:
            if computers_hand_value <= 15 or computers_hand_value < players_hand_value and players_hand_value <= 21:
                computers_hand.append(BF.Pick_random_cards(game_deck, 1))
                deals += 1
            else:
                deals += 1
                break
            
    print()
    # This function checks who will eat chicken dinner :D
    winner = BF.Return_winner_blackjack(players_hand_value, computers_hand_value)
    
    if winner == 1:
        print("You win!")
    elif winner == 2:
        print("Dealer wins!")
    elif winner == 3:
        print("Push!")

    aftergame_choice = input("\nDo you wish to QUIT('q') or START('s') another game?: ")

    if aftergame_choice == 'q':
        InGame = False
        os.system("clear")
    else:
        os.system("clear")

