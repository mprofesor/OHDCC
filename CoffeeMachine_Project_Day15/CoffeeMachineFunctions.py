# Functions simulator file
# OFF
# REFILL
# REPORT
# MAKE COFFEE

def Off():
    """Turning off the coffee machine"""
    print("Turning off...")
    return False

def Refill(substance, tank_volume):
    """Refill given substance to maximal volume"""
    substance = tank_volume
    print(f"Refilling...\ndone")
    return substance

def Report(resources, money):
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    """Print report of available resources"""
    report = f"""
    water: {water}ml
    milk: {milk}ml
    coffee: {coffee}g
    money: ${money}
    """
    return report

def MakeCoffee(machine_resources, coffee_ingredients, coffee_art, coffee_type):
    """Make coffee and remove used resources from machine resources"""
    resources_after = {}
    for resource in machine_resources:
        resources_after[resource] = machine_resources[resource] - coffee_ingredients[resource]
    
    message = f"""
    Preparing your {coffee_type}...
    Ready
    Please enjoy your coffee!
    {coffee_art}
    """
    print(message)
    return resources_after

def EnoughResources(resources, ingredients):
    """Check if there is enough resources to make coffee"""
    is_enough = True
    for resource in resources:
        if resources[resource] < ingredients[resource]:
            is_enough = False
    return is_enough
        
def WhatToRefill(resources, ingredients):
    """Check what need to be refilled in coffee machine"""
    resources_to_refill = []
    print("\nRefill this resources to make this type of coffee: ")
    for resource in resources:
        if resources[resource] < ingredients[resource]:
             resources_to_refill.append(resource)
    return "\n".join(resources_to_refill)
