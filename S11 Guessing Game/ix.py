import re


def get_yesOrNo(msg = "Yes or No? "):
    user_input = input(msg)
    if not isinstance(user_input, str):
        raise TypeError(f"user input '{user_input}' is not a string")

    if re.search("yes"[:len(user_input)], user_input, re.IGNORECASE):
        return True

    if re.search("no"[:len(user_input)], user_input, re.IGNORECASE):
        return False

    raise ValueError(f"user input '{user_input}' is not a 'yes' or 'no'")
    



def main():
    yesno()

if __name__ == "__main__":
    main()
    


    
    
