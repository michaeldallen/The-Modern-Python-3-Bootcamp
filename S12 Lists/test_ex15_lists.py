import pytest


from ex15_lists import get_my_stuff
from ex15_lists import get_nums


def test_my_stuff():
    ms = get_my_stuff()
    assert len(ms) >= 4


def test_my_stuff_has_a_string():
    ms = get_my_stuff()
    has_string = False
    for i in ms:
        if isinstance(i, str):
            has_string = True
            break
    assert has_string


def test_my_stuff_has_a_float():
    ms = get_my_stuff()
    has_float = False
    for i in ms:
        if isinstance(i, float):
            has_float = True
            break
    assert has_float


def test_nums_contains_1_through_99():
    mn = get_nums()
    i = 1
    while i <= 99:
        assert i in mn
        i += 1

