import random
import click

from ix import get_1to10
from ix import get_yesOrNo


def main():
    
    trying = True
    while trying:
        target = random.randint(1,10)
        tries = 0
        guess = 0
        while guess != target:
            guess = get_1to10()
            tries += 1
            if guess < target:
                print("too low")
            elif guess > target:
                print("too high")
            else:
                print(f"just right in {tries} tr{'y' if tries == 1 else 'ies'}")
        trying = get_yesOrNo("play again (y/n)? ")
            

if __name__ == "__main__":
    main()
    
