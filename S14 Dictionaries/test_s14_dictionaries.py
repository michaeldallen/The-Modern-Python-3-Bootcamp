import pytest
import random
from unittest.mock import MagicMock

from s14_dictionaries import createDict3
from s14_dictionaries import fullName
from s14_dictionaries import totalDonations
from s14_dictionaries import bakeryChoice
from s14_dictionaries import bakeryInStock
from s14_dictionaries import checkStock


def test_ex26_create():
    gazouta = createDict3()
    assert isinstance(gazouta, dict)
    assert len(gazouta) == 3


def test_ex27_fullName():

    gazinta = {
        "first": "Neil",
        "last": "Young",
    }
    expected_gazouta = "Neil Young"
    gazouta = fullName(gazinta)
    assert gazouta == expected_gazouta


def test_ex28_donations():
    gazinta = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                   stan=150.0, lisa=50.25, harrison=10.0)
    expected_gazouta = 436.74
    gazouta = totalDonations(gazinta)
    assert gazouta == expected_gazouta


def test_ex29_bakeryChoice(monkeypatch):
    monkeypatch.setattr(random, "choice", MagicMock(
        return_value="peanut butter Think! bar"))
    assert bakeryChoice() == "peanut butter Think! bar"


def test_ex29_bakeryInStock():
    assert not bakeryInStock("peanut butter Think! bar")
    assert bakeryInStock("tea cake")


def test_ex29_checkStockGood(monkeypatch):
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    checkStock("tea cake")
    mock_print.assert_called_once_with("25 left")


def test_ex29_checkStockBad(monkeypatch):
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    checkStock("peanut butter Think! bar")
    mock_print.assert_called_once_with("We don't make that")
