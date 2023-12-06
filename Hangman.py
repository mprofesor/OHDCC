import random
import os

# Word list
word_list = [
    'cat', 'dog', 'mouse', 'camel',
    'deer', 'candy', 'chocolate', 'sugar',
    'jelly', 'liquorice', 'biology', 'chemistry',
    'math', 'technology', 'history', 'water',
    'juice', 'beer', 'vodka', 'tea', 'cofee'
    ]

# ASCII ART
hangman_name = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/'''

hangman = [
'''
   ____
  |/   |
  |    O
  |   /|\ 
  |   / \ 
  |
-----
''',
'''
   ____
  |/   |
  |    O
  |   /|\ 
  |   / 
  |
-----
''',
'''
   ____
  |/   |
  |    O
  |   /|\ 
  |   
  |
-----
''',
'''
   ____
  |/   |
  |    O
  |   /|
  |   
  |
-----
''',
'''
   ____
  |/   |
  |    O
  |    |
  |   
  |
-----
''',
'''
   ____
  |/   |
  |    O
  |   
  |   
  |
-----
''',
'''
   ____
  |/   |
  |    
  |   
  |   
  |
-----
''',
'''
   ____
  |/   
  |    
  |   
  |   
  |
-----
''',
'''
   ____
  |   
  |    
  |   
  |   
  |
-----
''',
'''

  |
  |    
  |   
  |   
  |
-----
''', 
'''
   
   
     
    
   
  
-----
''',
'''
   
  
  
  
  


'''
]

# Most important variables
word = word_list[random.randint(0, len(word_list) - 1)]
word_to_guess = []
# This list needs to be dynamic
for letter in word:
    word_to_guess.append('_')
GameOver = False
Win = False
lives = 11
used_letters = []

# Print some ASCII ART :D
print(hangman_name)

# Main game loop
while not GameOver:
    Win = True # I'm later changing it to False to use only one for loop
    InWord = False
    guessed_letter = input("Guess a letter: ")
    os.system('clear')
    print()

    for i in range(0, len(word_to_guess)):
        if guessed_letter == word[i]:
            word_to_guess[i] = guessed_letter
            InWord = True
        if word_to_guess[i] == '_':
            Win = False

    if not InWord:
        used_letters.append(guessed_letter)
        lives -= 1
    
    if lives == 0:
        GameOver = True

    if Win == True:
        GameOver = True

    for letter in word_to_guess:
        print(letter, end=' ')
    print(hangman[lives])
    print("Used letters: ", end='')
    for letter in used_letters:
        print(letter, end=' ')
    print()

if Win == True:
    print("You win!")
else:
    print("You lose!")

# So this is my solution for creating the Hangman Game Project :D
# Not the prettiest but mine
