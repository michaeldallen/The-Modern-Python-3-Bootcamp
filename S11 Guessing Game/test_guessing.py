import pytest
from unittest.mock import MagicMock


# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch14s08.html
import sys


from guessing import getInputFrom1to10


def test_getInputFrom1to10_badType_string(monkeypatch):
    with pytest.raises(TypeError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value = "foo"))
        user_input = getInputFrom1to10(sys._getframe().f_code.co_name)


def test_getInputFrom1to10_badType_float(monkeypatch):
    with pytest.raises(TypeError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value = "1.1"))
        user_input = getInputFrom1to10(sys._getframe().f_code.co_name)



def test_getInputFrom1to10_badValue_tooLow(monkeypatch):
    with pytest.raises(ValueError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value = "0"))
        user_input = getInputFrom1to10(sys._getframe().f_code.co_name)


def test_getInputFrom1to10_badValue_tooHigh(monkeypatch):
    with pytest.raises(ValueError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value = "11"))
        user_input = getInputFrom1to10(sys._getframe().f_code.co_name)



def test_getInputFrom1to10_OK(monkeypatch):
    monkeypatch.setattr("builtins.input", MagicMock(return_value = "1"))
    user_input = getInputFrom1to10(sys._getframe().f_code.co_name)
    assert user_input == 1


@pytest.mark.skip()
def test_playAgain():
    assert(0)

@pytest.mark.skip()
def test_dontPlayAgain():
    assert(0)

    
