# Short Text game to train conditional statements version prealpha XD
print('''
            ___
        ,-""___""-.
       .;""'| |`"":.
       || | | | | ||
       ||_|_|_|_|_||
      //          /|
     /__         //|
 ,-""___""-.    //||
.;""'| |`"":.  //
||/| | | | || //
||_|_|_|_|_||//
||_________||/
||         ||
''         '' ''')
GameOver = False
Won = False
while not GameOver:
    print("\nWelcome to the ROOM OF DEATH...\n")
    print("...You have aweken from a strange dream...")
    print("But it turns out that you are no longer in YOUR ROOM!")
    choice = input("What you want to do 'leave' the bed or 'stay' in bed: ")
    if choice.lower() == 'leave':
        print("\nRight after your first feet touched the floor you felt dizzy and passed away for good.")
        GameOver = True
    elif choice.lower() == 'stay':
        print("\nFloor started turning into lava but your bed stand still.")
        print("\nYou have noticed long lamp that could help you swing to the doors and open them and maybe leave the room.")
        choice = input("\nWhat you want to do 'swing' or 'stay' in bed: ")
        if choice.lower() == 'swing':
            print("\nYou was not good at PE you swing and fall on the deadly floor and died.")
            GameOver = True
        elif choice.lower() == 'stay':
            print("\nYou stayed in your bed and survived.")
            print("\nYou have survived another round but your bed is starting to burn.")
            choice = input("\nWhat you are going to do: 'wake' from a dream 'stay' because it's a dream: ")
            if choice.lower() == 'wake':
                print("\nYou have awaken to a nightmare of your life and you died.")
                GameOver = True
            elif choice.lower() == 'stay':
                print("\nThe flames are no longer so you have survived again.")
                print("\nNow you know you need to stay in bed whatever is happening so you have WON!")
                GameOver = True
                Won = True
            else:
                print("\nYou did something stupid and died.")
                GameOver = True
        else:
            print("\nYou did something stupid and died.")
            GameOver = True
    else:
        print("\nYou did something stupid and died.")
        GameOver = True

    if Won == True:
        print("\n!!!YOU HAVE WON!!!\n")

    if GameOver == True:
        choice = input("\nGAME OVER do you wish to play again? 'Y'/'N': ")
        if choice == 'Y':
            GameOver = False
            Won = False
