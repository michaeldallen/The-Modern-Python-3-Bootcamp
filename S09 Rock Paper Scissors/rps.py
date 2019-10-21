
def get_rock_paper_scissors(msg):
    user_input = input(msg).lower()

    for rps in ("rock", "paper", "scissors"):
        if (rps.startswith(user_input)):
            return rps

    raise ValueError(f"don't understand user input '{user_input}'")



winner = {
    (    "rock",     "rock") :     "draw",
    (    "rock",    "paper") : "player 2",
    (    "rock", "scissors") : "player 1",

    (   "paper",     "rock") : "player 1",
    (   "paper",    "paper") :     "draw",
    (   "paper", "scissors") : "player 2",

    ("scissors",     "rock") : "player 2",
    ("scissors",    "paper") : "player 1",
    ("scissors", "scissors") :     "draw",
}

def shoot(player_1_input, player_2_input):
    return winner[(player_1_input, player_2_input)]





if __name__ == "__main__":
    while True:
        try:
            p1 = get_rock_paper_scissors("Player 1: rock, paper, or scissors? ")
            break
        except ValueError as err:
            print(err)
    print(f"Player 1 guesses '{p1}'")

    while True:
        try:
            p2 = get_rock_paper_scissors("Player 2: rock, paper, or scissors? ")
            break
        except ValueError as err:
            print(err)
    print(f"Player 2 guesses '{p2}'")

    print("SHOOT!")
    winner = shoot(p1, p2)
    if winner == "draw":
        print("draw")
    else:
        print(f"{winner} wins")

        
