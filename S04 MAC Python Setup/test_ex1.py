import pytest
from pytest import raises
from unittest.mock import MagicMock

def test_printYourName(monkeypatch):
    mock_print = MagicMock(return_value="your name b")
    monkeypatch.setattr("builtins.print", mock_print)
    print("your name a")
    mock_print.assert_called_once_with("your name")

