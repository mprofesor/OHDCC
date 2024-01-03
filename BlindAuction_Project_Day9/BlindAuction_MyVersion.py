import ASCII_ART
import os

# Print beautiful ASCII ART :D
print(ASCII_ART.gavel)

# Greet user
print(ASCII_ART.greet)

StopAuction = False
bidders = []

while not StopAuction:
        # Ask for the bid
        number_of_bidder = 0
        name = input("Please enter your name: ")
        bid = int(input("Please enter your bid: $"))

        # Place the name with the bid inside the list of dictionaries
        bidders.append({"name": name, "bid": bid})

        # Add another bidder? (while loop)
        choice = input("Do you wish to add another bidder? (YES/NO)")
        if choice == 'YES':
            number_of_bidder += 1
        elif choice == 'NO':
              StopAuction = True
        os.system("clear")

# print(bidders)

for i in range (0, len(bidders)):
    if i == 0:
        bid = bidders[0]["bid"]
        name = bidders[0]["name"]
    if i != 0:
        if bid < bidders[i]["bid"]:
            bid = bidders[i]["bid"]
            name = bidders[i]["name"]
    # print(f"{name} {bid}")

# Print the winner of the auction (the highest bid wins)
print(f"The winner is {name} with the bid ${bid}!")