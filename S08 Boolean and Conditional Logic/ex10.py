# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


def find_food_group(food):
    if("apple" == food or "grape" == food):
        print("fruit")
    elif("bacon" == food or "steak" == food):
        print("meat")
    elif("dirt" == food or "worm" == food):
        print("")


    
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if __name__ == "__main__":
    find_food_group("bacon")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

