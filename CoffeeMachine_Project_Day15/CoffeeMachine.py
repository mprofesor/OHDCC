# Main simulator file
import ASCII_ART as AA
import CoffeeMachineFunctions as SF
import CoffeeMachineData as SD
import os

# Main simulator function
def CoffeeMachine():
    machine_resources = SD.resources
    machine_money = 0
    power = True
    while power:
        os.system("clear")
        # Print beautiful ASCII ART
        print(AA.COFFEE_MACHINE)
        function = input("What would you like? (espresso/latte/cappuccino): ")
        if function == "espresso" or function == "latte" or function == "cappuccino":
            coffee_type = function
            coffee_ingredients = SD.MENU[coffee_type]["ingredients"]
            if SF.EnoughResources(machine_resources, coffee_ingredients):
                if coffee_type == "espresso":
                    coffee_art = AA.ESPRESSO
                elif coffee_type == "cappuccino":
                    coffee_art = AA.CAPPUCCINO
                elif coffee_type == "latte":
                    coffee_art = AA.LATTE
                else:
                    coffee_art = ""
                
                coffee_cost = SD.MENU[coffee_type]["cost"]
                print("Please insert the coins")
                pennies = float(input("Pennies: "))
                nickles = float(input("Nickles: "))
                dimes = float(input("Dimes: "))
                quarters = float(input("Quarters: "))

                user_money = 0.01 * pennies + 0.05 * nickles + 0.1 * dimes + 0.25 * quarters
                print(f"Credit: {user_money}")
                if user_money >= coffee_cost:
                    machine_resources = SF.MakeCoffee(machine_resources, coffee_ingredients, coffee_art, coffee_type)
                    change = round(user_money - coffee_cost, 2)
                    machine_money += coffee_cost
                    if change:
                        print(f"Here is your ${change} change")
                else:
                    print(f"Not enough money for {coffee_type}. Refunding...")
            elif not SF.EnoughResources(machine_resources, coffee_ingredients):
                short_report = SF.WhatToRefill(machine_resources, coffee_ingredients)
                print(short_report)
        elif function == "report":
            report = SF.Report(machine_resources, machine_money)
            print(report)
        elif function == "refill":
            resource_refill = input("What do you want to refill? (water/milk/coffee): ")
            if resource_refill == "water" or resource_refill == "milk" or resource_refill == "coffee":
                machine_resources[resource_refill] = SF.Refill(resource_refill, SD.resources[resource_refill])
            else:
                print(f"There is no such thing in coffee machine as {resource_refill}.")
        elif function == "off":
            power = SF.Off()
        
        if power:
            input("STAND BY... Please enter anything to use machine")







CoffeeMachine()
