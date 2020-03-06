import pytest
from unittest.mock import MagicMock

from functions import make_noise
from functions import speak_pig
from functions import generate_evens
from functions import yell


def test_make_noise(monkeypatch):
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    make_noise()
    mock_print.assert_called_once_with("THE CROWD GOES WILD")


def test_speak_pig(monkeypatch):
    expected_gazouta = "oink"
    gazouta = speak_pig()
    assert gazouta == expected_gazouta


def test_generate_evens():
    expected_gazouta = [
             2,  4,  6,  8,
        10, 12, 14, 16, 18,
        20, 22, 24, 26, 28,
        30, 32, 34, 36, 38,
        40, 42, 44, 46, 48,
    ]
    gazouta = generate_evens()
    assert gazouta == expected_gazouta


yell_test_data = [
    ("foo", "FOO!"),
    ("go away", "GO AWAY!"),
    ("leave me alone", "LEAVE ME ALONE!"),
]
        
@pytest.mark.parametrize("user_input,expected_output", yell_test_data)
def test_yell(user_input, expected_output):
    gazouta = yell(user_input)
    assert gazouta == expected_output
    
