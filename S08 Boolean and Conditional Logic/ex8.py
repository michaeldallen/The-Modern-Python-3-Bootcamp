# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------

def lucky(choice):
    # YOUR CODE GOES HERE:
    if(7 == choice):
        print(f"lucky {choice}")
    else:
        print(f"unlucky {choice}")

if __name__ == "__main__":
    lucky(choice)
    
