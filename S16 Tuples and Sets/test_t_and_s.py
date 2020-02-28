import pytest

from t_and_s import numbers
from t_and_s import value
from t_and_s import static_values
from t_and_s import unique_stuff


def test_numbers():
    expected_gazouta = (1, 2, 3, 4)
    gazouta = numbers()
    assert gazouta == expected_gazouta


def test_value():
    expected_gazouta = (1,)
    assert isinstance(expected_gazouta, tuple)
    gazouta = value()
    assert gazouta == expected_gazouta


def test_static_values():
    gazinta = [10, 20, 30]
    expected_gazouta = (10, 20, 30)
    gazouta = static_values(gazinta)
    assert gazouta == expected_gazouta


def test_unique_stuff():
    gazinta = [1, 3, 1, 5, 2, 5, 1, 2, 5]
    expected_gazouta = {1, 2, 3, 5}
    gazouta = unique_stuff(gazinta)
    assert gazouta == expected_gazouta
