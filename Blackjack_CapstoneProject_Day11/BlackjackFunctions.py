import random

def Pick_random_cards(deck_list, number_of_cards):
    """
    This function takes one list deck_list(list) of cards 
    and picks number_of_cards(int) random cards.
    It returns list of number_of_cards(int) random cards from deck.
    """
    picked_cards = []
    for i in range(number_of_cards):
        picked_card = random.choice(deck_list)
        picked_cards.append(picked_card)
        deck_list.remove(picked_card)

    if number_of_cards > 1:
        return picked_cards
    else:
        return picked_cards[0] 


def Value_the_hand(hand, deck_dictionary, hand_value):
    """
    This function values the hand based on the hand(list of cards)
    deck_dictionary(carefully prepared dictionary from ASCII_ART file)
    hand_value(int) initial hand value
    """
    for i in range(len(hand)):
        if "Heart_ace" == hand[i] or "Diamonds_ace" == hand[i] or "Clubs_ace" == hand[i] or "Spades_ace" == hand[i]:
            if hand_value < 11:
                hand_value += deck_dictionary[hand[i]]["Value_below11"]
            else:
                hand_value += deck_dictionary[hand[i]]["Value_over11"]
        else:
            hand_value += deck_dictionary[hand[i]]["Value"]
        
    return hand_value


def Value_firstround_dealers_hand(hand, deck_dictionary, hand_value):
    """
    Almost the same as the Value_the_hand function but for the dealers first 
    round hand
    """
    if "Heart_ace" == hand[0] or "Diamonds_ace" == hand[0] or "Clubs_ace" == hand[0] or "Spades_ace" == hand[0]:
        if hand_value < 11:
            hand_value += deck_dictionary[hand[0]]["Value_below11"]
        else:
            hand_value += deck_dictionary[hand[0]]["Value_over11"]
    else:
        hand_value += deck_dictionary[hand[0]]["Value"]
        
    return hand_value


def Retrive_cards_art(hand, deck_dictionary):
    """
    This function creates visual balckjack hand using ASCII ART.
    """
    hand_art = ""
    for i in range(len(hand)):
        hand_art += deck_dictionary[hand[i]]["Art"]
        hand_art += hand[i]

    return hand_art


def Retrive_firstround_dealers_hand_art(hand, deck_dictionary):
    """
    This function is simmilar to the Retrive_cards_art function.
    """
    hand_art = ""
    for i in range(2):
        if i == 0:
            hand_art += deck_dictionary[hand[i]]["Art"]
            hand_art += hand[i]
        elif i == 1:
            hand_art += deck_dictionary[hand[i]]["Headown_Art"]

    return hand_art


def Return_winner_blackjack(player1_score, player2_score):
    """
    This function determines winner from two players.
    If the player 1 wins return 1 else if player 2 wins returns 2 else returns 3.
    """
    if player1_score > 21 and player2_score <= 21:
        return 2
    elif player1_score <= 21 and player2_score > 21:
        return 1
    elif player1_score > 21 and player2_score > 21:
        return 3

    if player1_score == player2_score:
        return 3
    elif player1_score > player2_score:
        return 1
    elif player1_score < player2_score:
        return 2
    
