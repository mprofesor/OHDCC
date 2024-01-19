# Game Functions file

def ReturnName(list_of_dictionaries, index):
    """Return name(string)"""
    return list_of_dictionaries[index]["name"]

def ReturnFollowerCount(list_of_dictionaries, index):
    """Return follower_count(integer)"""
    return list_of_dictionaries[index]["follower_count"]

def ReturnDescription(list_of_dictionaries, index):
    """Return description(string)"""
    return list_of_dictionaries[index]["description"]

def ReturnCountry(list_of_dictionaries, index):
    """Return country(string)"""
    return list_of_dictionaries[index]["country"]

def PrintAccount(name, country, description, account_letter):
    """Prints the comparing message"""
    message = f"Compare {account_letter}: {name}, a {description}, from {country}."
    return message
