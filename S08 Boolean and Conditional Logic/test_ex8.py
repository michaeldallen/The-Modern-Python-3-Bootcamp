import pytest
from unittest.mock import MagicMock

from ex8 import lucky


@pytest.mark.parametrize("number,result", [(1, "unlucky"), (7, "lucky"), (10, "unlucky")])
def test_luck(number, result, monkeypatch):
    print(f"number: {number}, result: {result}")
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    lucky(number)
    mock_print.assert_called_once_with(result + " " + str(number))
                         
