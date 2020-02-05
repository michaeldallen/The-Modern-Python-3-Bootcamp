import pytest


from s12_lists import get_my_stuff
from s12_lists import get_nums


def test_ex15_my_stuff():
    ms = get_my_stuff()
    assert len(ms) >= 4


def test_ex15_my_stuff_has_a_string():
    ms = get_my_stuff()
    has_string = False
    for i in ms:
        if isinstance(i, str):
            has_string = True
            break
    assert has_string


def test_ex15_my_stuff_has_a_float():
    ms = get_my_stuff()
    has_float = False
    for i in ms:
        if isinstance(i, float):
            has_float = True
            break
    assert has_float


def test_ex15_nums_contains_1_through_99():
    mn = get_nums()
    i = 1
    while i <= 99:
        assert i in mn
        i += 1



from s12_lists import thisForThat


def test_ex16_thisForThat_singleElementHit():
    assert thisForThat(["Hanna"]) == ["Hannah"]
    assert thisForThat(["Geoffrey"]) == ["Jeffrey"]
    assert thisForThat(["aparna"]) == ["Aparna"]

def test_ex16_thisForThat_singleElementMiss():        
    assert thisForThat(["foo"]) == ["foo"]
    assert thisForThat(["bar"]) == ["bar"]

def test_ex16_thisForThat_multiElementMixed():    
    assert thisForThat(["foo", "bar", "baz"]) == ["foo", "bar", "baz"]

    raw = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]
    cooked = ["Hannah", "Louisa", "Claudia", "Angela", "Jeffrey", "Aparna"]
    assert thisForThat(raw) == cooked





from s12_lists import mashUC

def test_ex17_mashUC():

    expected_result = "SUPERCALIFRAGILISTICEXPIALIDOCIOUS"

    sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
    result = mashUC(sounds)

    assert result == expected_result
