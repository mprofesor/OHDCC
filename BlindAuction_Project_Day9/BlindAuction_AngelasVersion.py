import ASCII_ART
import os

# Print beautiful ASCII ART :D
print(ASCII_ART.gavel)

# Greet user
print(ASCII_ART.greet)

bids = {}
bidding_finished = False

def pick_highest_bid(bidding_record):
    # bidding_record = {"Angela": 123, "James": 321}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}!")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any otheer bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
    else:
        os.system("clear")

pick_highest_bid(bids)