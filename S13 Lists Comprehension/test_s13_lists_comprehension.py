from s13_lists_comprehension import bootstrap
from s13_lists_comprehension import evens
from s13_lists_comprehension import firstLetter
from s13_lists_comprehension import intersection
from s13_lists_comprehension import reversal
from s13_lists_comprehension import divBy12
from s13_lists_comprehension import amaze
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


def test_ex21_intersection():
    gazinta1 = list(range(1, 5))
    gazinta2 = list(range(3, 7))
    expected_gazouta = list(range(3, 5))
    gazouta = intersection(gazinta1, gazinta2)
    assert gazouta == expected_gazouta


def test_ex21_reversal():
    gazinta = ["Elie", "Tim", "Matt"]
    expected_gazouta = ["eile", "mit", "ttam"]
    gazouta = reversal(gazinta)
    assert gazouta == expected_gazouta


def test_ex22_divBy12():
    gazinta = list(range(1, 101))
    expected_gazouta = [12, 24, 36, 48, 60, 72, 84, 96]
    gazouta = divBy12(gazinta)
    assert gazouta == expected_gazouta


def test_ex23_amaze():
    gazinta = "amazing"
    expected_gazouta = list("mzng")
    gazouta = amaze(gazinta)
    assert gazouta == expected_gazouta
