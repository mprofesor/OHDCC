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

def Retrive_cards_art(hand, deck_dictionary):
    hand_art = ""
    for i in range(len(hand)):
        hand_art += deck_dictionary[hand[i]]["Art"]
        hand_art += hand[i]

    return hand_art
    
