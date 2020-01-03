import random

def suffix(i):
    if i > 10 and i < 20:
        return "th"
    elif i % 10 == 1:
        return "st"
    elif i % 10 == 2:
        return "nd"
    elif i % 10 == 3:
        return "rd"
    else:
        return "th"

def whenIsFive():
    i = 1
    while not random.randint(1,10) == 5:
        i += 1
    return i


def main():
    f = whenIsFive()
    suffix(f)
    print(f"got a five on the {f}{suffix(f)} try")


if __name__ == "__main__":
    main()


    

