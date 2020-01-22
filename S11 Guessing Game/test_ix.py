import pytest
from unittest.mock import MagicMock

from ix import get_yesOrNo

def test_getYesOrNo_badType(monkeypatch):
    with pytest.raises(TypeError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value = 1))
        get_yesOrNo()

def test_getYesOrNo_badValue(monkeypatch):
    with pytest.raises(ValueError) as e:
        monkeypatch.setattr("builtins.input", MagicMock(return_value = "maybe"))
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
    monkeypatch.setattr("builtins.input", MagicMock(return_value = user_input))
    result = get_yesOrNo()
    assert result == expected_result

    
    
