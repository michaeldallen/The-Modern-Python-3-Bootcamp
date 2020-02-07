import random


def createDict3():
    return {"a": None, "b": None, "c": None}


def fullName(artist):
    full_name = ' '.join([artist["first"], artist["last"]])
    return full_name


def totalDonations(donations):
    total_donations = sum(i for i in donations.values())
    return total_donations


def bakeryChoice():
    food = random.choice(
        ["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])
    return food


def bakeryInStock(item):
    bakery_stock = {
        "almond croissant": 12,
        "toffee cookie": 3,
        "morning bun": 1,
        "chocolate chunk cookie": 9,
        "tea cake": 25
    }
    if bakery_stock.get(item):
        return bakery_stock[item]
    else:
        return None


def checkStock(item = None):
    if not item:
        item = bakeryChoice()
        
    stock = bakeryInStock(item)
    if stock == None:
        print("We don't make that")
    else:
        print(f"{stock} left")




