import pytest

from s14_dictionaries import createDict3
from s14_dictionaries import fullName
from s14_dictionaries import totalDonations


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
