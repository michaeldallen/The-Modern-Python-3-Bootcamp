from s13_lists_comprehension import bootstrap
from s13_lists_comprehension import evens
from s13_lists_comprehension import firstLetter
import pytest


def test_ex20_bootstrap():
    assert bootstrap() == "bootstrap"


def test_ex20_firstLetter():
    gazinta = ["Elie", "Tim", "Matt"]
    expected_gazouta = ["E", "T", "M"]
    gazouta = firstLetter(gazinta)
    assert gazouta == expected_gazouta


def test_ex20_evens():
    gazinta = [1, 2, 3, 4, 5, 6]
    expected_gazouta = [2, 4, 6]
    gazouta = evens(gazinta)
    assert gazouta == expected_gazouta
