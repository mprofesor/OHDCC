from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Print report.
# Check resources sufficient
# Process coins
# Check reansaction successful
# Make Coffee

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    order = input(f"What would you like? ({options}): ")

    if menu.find_drink(order):
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        is_on = False

