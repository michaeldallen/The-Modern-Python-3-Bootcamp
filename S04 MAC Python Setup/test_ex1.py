import pytest
from pytest import raises
from unittest.mock import MagicMock

def test_printYourName(monkeypatch):
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    print("your name")
    mock_print.assert_called_once_with("your name")

