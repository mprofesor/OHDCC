# This is simple Rock Paper Scissors game that you can play against computer
import random

# ASCII ART *_*
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

graphics_moves = [rock, paper, scissors]
computer_rand_choice = random.randint(0, 2)

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(graphics_moves[your_choice])
print("Computer choice: \n")
print(graphics_moves[computer_rand_choice])


# IMO can be simplified but I don't have any good and fast idea for that
if your_choice == computer_rand_choice:
    print("Draw!")
elif your_choice == 0:
    if computer_rand_choice == 1:
        print("You lose")
    else:
        print("You win")
elif your_choice == 1:
    if computer_rand_choice == 0:
        print("You win")
    else:
        print("You lose")
elif your_choice == 2:
    if computer_rand_choice == 1:
        print("You win")
    else:
        print("You lose")
