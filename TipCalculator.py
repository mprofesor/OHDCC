#TIPCALCULATOR

#Print welcome to the jungele
print("Welcome to the tip calculator")
#variable bill = total cost of bill
#float because it's not necessarily integer number
bill = float(input("What was the total bill? "))
#variable people = ammount of people
#int because the output cannot be string. It can only be integer number
people = int(input("How many people to split the bill? "))
#varialbe tip = 0
tip = 0
#If the output of Tip is any other than 10,12 or 15 the input of Tip is not gonna be saved
#and program is gonna ask for input again.
while -10:
    tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
    if tip == 10:
        break
    elif tip == 12:
        break
    elif tip == 15:
        break
#variable cost = liczonko
cost = round(float((bill + (bill * tip/100))/people), 2)
#print answer
print("Each person should pay: " + "$" + str(cost)) 
