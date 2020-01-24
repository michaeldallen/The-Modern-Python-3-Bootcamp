
from unittest.mock import MagicMock
import pytest
import sys


# "Determining the Name of the Current Function"
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch14s08.html


from ix import get_1to10
from ix import get_yesOrNo


def test_getYesOrNo_badType(monkeypatch):
    with pytest.raises(TypeError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value=1))
        get_yesOrNo()


def test_getYesOrNo_badValue(monkeypatch):
    with pytest.raises(ValueError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value="maybe"))
        get_yesOrNo()


getYesOrNo_test_data = [

    ("yes",  True),
    ("y",    True),
    ("Yes",  True),
    ("Y",    True),
    ( "no", False),
    (  "n", False),
    ( "No", False),
    (  "N", False),

]


@pytest.mark.parametrize("user_input,expected_result", getYesOrNo_test_data)
def test_getYesOrNo(user_input, expected_result, monkeypatch):
    monkeypatch.setattr("builtins.input", MagicMock(return_value=user_input))
    result = get_yesOrNo()
    assert result == expected_result


def test_get_1to10_badType_string(monkeypatch):
    with pytest.raises(TypeError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value="foo"))
        get_1to10(sys._getframe().f_code.co_name)


def test_get_1to10_badType_float(monkeypatch):
    with pytest.raises(TypeError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value="1.1"))
        get_1to10(sys._getframe().f_code.co_name)


def test_get_1to10_badValue_tooLow(monkeypatch):
    with pytest.raises(ValueError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value="0"))
        get_1to10(sys._getframe().f_code.co_name)


def test_get_1to10_badValue_tooHigh(monkeypatch):
    with pytest.raises(ValueError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value="11"))
        get_1to10(sys._getframe().f_code.co_name)


def test_get_1to10_OK(monkeypatch):
    monkeypatch.setattr("builtins.input", MagicMock(return_value="1"))
    user_input = get_1to10(sys._getframe().f_code.co_name)
    assert user_input == 1

