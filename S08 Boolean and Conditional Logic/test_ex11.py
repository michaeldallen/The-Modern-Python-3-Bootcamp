import pytest

from unittest.mock import MagicMock

from ex11 import positive_or_negative

pos_neg_test_data = [
    ( 1,  1, "both positive"),
    (-1, -1, "both negative"),
    ( 1, -1, "x is positive and y is negative"),
    (-1,  1, "y is positive and x is negative"),
]


@pytest.mark.parametrize("x,y,expected_result", pos_neg_test_data)
def test_positive_or_negative(x, y, expected_result, monkeypatch):
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    positive_or_negative(x, y)
    mock_print.assert_called_once_with(expected_result)

    
    
