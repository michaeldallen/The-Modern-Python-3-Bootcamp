import re


def get_yesOrNo(msg="Yes or No? "):
    user_input = input(msg)
    if not isinstance(user_input, str):
        raise TypeError(f"user input '{user_input}' is not a string")

    if re.search("yes"[:len(user_input)], user_input, re.IGNORECASE):
        return True

    if re.search("no"[:len(user_input)], user_input, re.IGNORECASE):
        return False

    raise ValueError(f"user input '{user_input}' is not a 'yes' or 'no'")


def get_1to10(msg="Guess a number from 1 to 10: "):
    raw_user_input = input(msg)
    if not raw_user_input.isdigit():
        raise TypeError(f"user input '{raw_user_input}' is not an integer")

    user_input = int(raw_user_input)

    if user_input < 1:
        raise ValueError(f"user input '{user_input}' must be greater than one")

    if user_input > 10:
        raise ValueError(f"user input '{user_input}' must be less than ten")

    return user_input





