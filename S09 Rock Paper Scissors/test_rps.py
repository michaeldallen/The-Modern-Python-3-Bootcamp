import pytest
from unittest.mock import MagicMock

from rps import get_rock_paper_scissors
from rps import shoot
from rps import getRandomChoice

rps_positive_test_data = [
    
    (    "rock",     "rock"),
    (     "roc",     "rock"),
    (      "ro",     "rock"),
    (       "r",     "rock"),
    
    (   "paper",    "paper"),
    (    "pape",    "paper"),
    (     "pap",    "paper"),
    (      "pa",    "paper"),
    (       "p",    "paper"),
    
    ("scissors", "scissors"),
    ( "scissor", "scissors"),
    (  "scisso", "scissors"),
    (   "sciss", "scissors"),
    (    "scis", "scissors"),
    (     "sci", "scissors"),
    (      "sc", "scissors"),
    (       "s", "scissors"),
    
]

@pytest.mark.parametrize("user_input,expected_result", rps_positive_test_data)
def test_getGoodRockPaperScissors(user_input, expected_result, monkeypatch):
    mock_input = MagicMock(return_value = user_input)
    monkeypatch.setattr("builtins.input", mock_input)
    result = get_rock_paper_scissors(f"checking '{user_input}', expecting '{expected_result}'")
    assert result == expected_result


rps_negative_test_data = [

    (""),
    ("bar"),
    ("foo"),
    ("or"),
    ("party"),

    ("rocket"),
    ("rook"),

    ("ape"),
    ("papered"),

    ("scientist"),

]

@pytest.mark.parametrize("user_input", rps_negative_test_data)
def test_getBadRockPaperScissors(user_input, monkeypatch):
    mock_input = MagicMock(return_value = user_input)
    monkeypatch.setattr("builtins.input", mock_input)

    with pytest.raises(ValueError):
        get_rock_paper_scissors(f"checking '{user_input}', expecting 'Exception'")



    
rps_shoot_test_data = [

    (    "rock",     "rock",     "draw"),
    (    "rock",    "paper", "player 2"),
    (    "rock", "scissors", "player 1"),

    (   "paper",     "rock", "player 1"),
    (   "paper",    "paper",     "draw"),
    (   "paper", "scissors", "player 2"),

    ("scissors",     "rock", "player 2"),
    ("scissors",    "paper", "player 1"),
    ("scissors", "scissors",     "draw"),

]

@pytest.mark.parametrize("player_1_input,player_2_input,winner", rps_shoot_test_data)
def test_shoot(player_1_input, player_2_input, winner, monkeypatch):
    
    mock_player_1_input = MagicMock(return_value = player_1_input)
    monkeypatch.setattr("builtins.input", mock_player_1_input)
    p1 = get_rock_paper_scissors(f"get player 1 input '{player_1_input}'")
    
    mock_player_2_input = MagicMock(return_value = player_2_input)
    monkeypatch.setattr("builtins.input", mock_player_2_input)
    p2 = get_rock_paper_scissors(f"get player 2 input '{player_2_input}'")

    assert shoot(p1, p2) == winner


def test_getRandomChoice():
    for x in range(10):
        c = getRandomChoice()
        print(f"random choice is {c}")
        assert c in ("rock", "paper", "scissors")
    
    
