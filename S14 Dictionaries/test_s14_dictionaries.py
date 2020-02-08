import pytest
import random
from unittest.mock import MagicMock

from s14_dictionaries import createDict3
from s14_dictionaries import fullName
from s14_dictionaries import totalDonations
from s14_dictionaries import bakeryChoice
from s14_dictionaries import bakeryInStock
from s14_dictionaries import checkStock
from s14_dictionaries import getInitialGameState
from s14_dictionaries import cookies


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


def test_ex29_checkStockGood2(monkeypatch):
    bun = MagicMock(return_value="morning bun")
    monkeypatch.setattr(random, "choice", bun)
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    checkStock()
    mock_print.assert_called_once_with("1 left")


def test_ex29_checkStockBad(monkeypatch):
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    checkStock("peanut butter Think! bar")
    mock_print.assert_called_once_with("We don't make that")


def test_ex30_fromKeys():
    gazinta = [
        "current_score",
        "high_score",
        "number_of_lives",
        "items_in_inventory",
        "power_ups",
        "ammo",
        "enemies_on_screen",
        "enemy_kills",
        "enemy_kill_streaks",
        "minutes_played",
        "notifications",
        "achievements",
    ]
    expected_gazouta = {
        'current_score': 0,
        'high_score': 0,
        'number_of_lives': 0,
        'items_in_inventory': 0,
        'power_ups': 0,
        'ammo': 0, 'enemies_on_screen': 0,
        'enemy_kills': 0,
        'enemy_kill_streaks': 0,
        'minutes_played': 0,
        'notifications': 0,
        'achievements': 0,
    }
    gazouta = getInitialGameState(gazinta)
    assert gazouta == expected_gazouta


def test_ex30_cookies():
    gazinta = {
        'croissant': 19,
        'bagel': 4,
        'muffin': 8,
        'cake': 1,
    }
    initial_gazinta = gazinta.copy()
    expected_gazouta = {
        'croissant': 19,
        'bagel': 4,
        'muffin': 8,
        'cookie': 18,
    }
    gazouta = cookies(gazinta)
    assert gazinta == initial_gazinta
    assert gazouta == expected_gazouta
    
