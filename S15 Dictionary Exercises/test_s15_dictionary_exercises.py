import pytest

from s15_dictionary_exercises import abbreviations_for
from s15_dictionary_exercises import list_to_dict
from s15_dictionary_exercises import vowels
from s15_dictionary_exercises import ascii

def test_abbreviations_for():
    gazinta1 = ["CA", "NJ", "RI"]
    gazinta2 = ["California", "New Jersey", "Rhode Island"]
    expected_gazouta = {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}
    gazouta = gazaouta = abbreviations_for(gazinta1, gazinta2)
    assert gazouta == expected_gazouta


def test_list_to_dict():
    gazinta = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
    expected_gazouta =  {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
    gazouta = list_to_dict(gazinta)
    assert gazouta == expected_gazouta


def test_vowels():
    expected_gazouta = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    gazouta = vowels()
    assert gazouta == expected_gazouta


def test_ascii():
    expected_gazouta = {
        65: 'A',
        66: 'B',
        67: 'C',
        68: 'D',
        69: 'E',
        70: 'F',
        71: 'G',
        72: 'H',
        73: 'I',
        74: 'J',
        75: 'K',
        76: 'L',
        77: 'M',
        78: 'N',
        79: 'O',
        80: 'P',
        81: 'Q',
        82: 'R',
        83: 'S',
        84: 'T',
        85: 'U',
        86: 'V',
        87: 'W',
        88: 'X',
        89: 'Y',
        90: 'Z',
    }
    gazouta = ascii()
    assert gazouta == expected_gazouta

    
