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




from s12_lists import embiggenList

def test_ex18_embiggenList():
    l = []
    lprime = embiggenList(l, "a")
    assert lprime == ["a"]

    l = lprime
    lprime = embiggenList(l, "b")
    assert lprime == ["a", "b"]


    instructors = []
    instructors = embiggenList(instructors, "Colt")
    instructors = embiggenList(instructors, "Blue")
    instructors = embiggenList(instructors, "Lisa")
    assert instructors == ["Colt", "Blue", "Lisa"]
                                    

    
    



from s12_lists import listRemoveFirst

def test_ex19_listRemoveFirst():

    instructors = [
        "Colt",
        "Blue",
        "Lisa",
    ]
    
    gazinta = instructors
    expected = [
        "Blue",
        "Lisa",
    ]
    gazouta = listRemoveFirst(gazinta)
    assert gazouta == expected

    gazouta = listRemoveFirst([])
    assert gazouta == None



from s12_lists import listRemoveLast

def test_ex19_listRemoveLast():

    instructors = [
        "Colt",
        "Blue",
        "Lisa",
    ]

    gazinta = instructors
    expected = [
        "Colt",
        "Blue",
    ]
    gazouta = listRemoveLast(gazinta)
    assert gazouta == expected

    gazouta = listRemoveLast([])
    assert gazouta == None
    

from s12_lists import listAddLast

    
def test_ex19_listAddLast():

    instructors = [
        "Colt",
        "Blue",
        "Lisa",
    ]

    gazinta = instructors
    
    expected = [
        "Colt",
        "Blue",
        "Lisa",
        "Done",
    ]
    gazouta = listAddLast(gazinta, "Done")
    assert gazouta == expected

    gazouta = listAddLast([], "Done")
    assert gazouta == ["Done"]
    
    
    
from s12_lists import listAddFirst

    
def test_ex19_listAddFirst():

    instructors = [
        "Colt",
        "Blue",
        "Lisa",
    ]

    gazinta = instructors
    
    expected = [
        "Done",
        "Colt",
        "Blue",
        "Lisa",
    ]
    gazouta = listAddFirst(gazinta, "Done")
    assert gazouta == expected

    gazouta = listAddFirst([], "Done")
    assert gazouta == ["Done"]
    
    
    
    
    
    
