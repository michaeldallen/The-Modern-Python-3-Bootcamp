import pytest
from unittest.mock import MagicMock

from ex9 import am_i_odd


even_odd_test_data = [
    (260, "even"),
    (953,  "odd"),
    (715,  "odd"),
    ( 59,  "odd"),
    (500, "even"),
    (393,  "odd"),
    (526, "even"),
    (311,  "odd"),
    (739,  "odd"),
]



@pytest.mark.parametrize("number,result", even_odd_test_data)
def test_oddity(number, result, monkeypatch):
    print(f"number: {number}, result: {result}")
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    am_i_odd(number)
    mock_print.assert_called_once_with(str(number) + " is " + result)
                         
